import streamlit as st
import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors

# config page
st.set_page_config(page_title="Boutique BDE", page_icon="🛍️", layout="wide")

# init panier
if 'cart' not in st.session_state:
    st.session_state.cart = []

# cache donneées et modèle
@st.cache_resource
def load_data_and_model():
    
    # chargement csv
    df_products = pd.read_csv('products.csv')
    df_orders = pd.read_csv('order_products.csv') 
    
    # nettoyage
    df_orders = df_orders.dropna(subset=['order_id', 'product_id'])
    df_orders = df_orders.drop_duplicates(subset=['order_id', 'product_id'])
    
    # echantillonnage par panier (opti ram)
    if len(df_orders) > 500000:
        paniers_aleatoires = pd.Series(df_orders['order_id'].unique()).sample(50000, random_state=42)
        df_orders = df_orders[df_orders['order_id'].isin(paniers_aleatoires)]
        
    # creation matrice creuse
    product_c = pd.Categorical(df_orders['product_id'])
    order_c = pd.Categorical(df_orders['order_id'])
    
    row = product_c.codes
    col = order_c.codes
    data = np.ones(len(df_orders))
    
    item_matrix = csr_matrix((data, (row, col)), shape=(len(product_c.categories), len(order_c.categories)))
    
    # entrainement knn
    knn_model = NearestNeighbors(metric='cosine', algorithm='brute', n_neighbors=4)
    knn_model.fit(item_matrix)
    
    return df_products, knn_model, product_c, item_matrix

# recup data
df_products, knn_model, product_c, item_matrix = load_data_and_model()

# prediction knn
def get_recommendations(product_id, n_recommandations=3):
    
    # verif existence produit
    if product_id not in product_c.categories:
        return []
        
    # index et vecteur produit
    product_idx = product_c.categories.get_loc(product_id)
    product_vector = item_matrix[product_idx].reshape(1, -1)
    
    # calcul plus proches voisins
    distances, indices = knn_model.kneighbors(product_vector, n_neighbors=n_recommandations + 1)
    reco_names = []
    
    # map index vers noms
    for i in range(1, len(distances.flatten())):
        idx_voisin = indices.flatten()[i]
        id_produit_voisin = product_c.categories[idx_voisin]
        
        nom_produit = df_products[df_products['product_id'] == id_produit_voisin]['product_name'].values
        
        if len(nom_produit) > 0:
            reco_names.append(nom_produit[0])
            
    return reco_names

# popup action panier
@st.dialog("🛒 Panier mis à jour !")
def ajout_panier_popup(product_id, product_name):
    
    # recapitulatif
    st.success(f"**{product_name}** a été ajouté à votre panier avec succès.")
    st.write(f"📦 **Résumé :** Vous avez actuellement **{len(st.session_state.cart)} article(s)** dans votre panier")
    
    st.divider()
    
    # affichage recos
    st.subheader("Recommendations :")
    recommandations = get_recommendations(product_id)
    
    if recommandations:
        for reco in recommandations:
            st.write(f"-> {reco}")
    else:
        st.write("Pas de suggestion pour cet article")
        
    # close popup
    if st.button("Continuer mes achats"):
        st.rerun()

# vue sidebar
with st.sidebar:
    
    st.header("Panier")
    
    # affichage contenu panier
    if len(st.session_state.cart) == 0:
        st.info("Votre panier est vide.")
    else:
        for i, article in enumerate(st.session_state.cart):
            st.write(f"{i+1}. {article}")
            
        st.divider()
        
        # clear panier
        if st.button("Vider le panier"):
            st.session_state.cart = []
            st.rerun()

# vue principale
st.title("Boutique en ligne")

# search bar
search_term = st.text_input("Recherche :", "")

# resultat recherche
if search_term:
    
    # filtre produits
    results = df_products[df_products['product_name'].str.contains(search_term, case=False, na=False)].head(10)
    
    if len(results) == 0:
        st.warning("Aucun article trouvé")
    else:
        st.write("### Résultats :")
        
        # liste elements
        for _, row in results.iterrows():
            col1, col2 = st.columns([4, 1])
            
            with col1:
                st.write(f"**{row['product_name']}**")
                
            with col2:
                # trigger event panier
                if st.button("Ajouter", key=row['product_id']):
                    st.session_state.cart.append(row['product_name'])
                    ajout_panier_popup(row['product_id'], row['product_name'])
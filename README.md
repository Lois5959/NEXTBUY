🛒 NEXTBUY : De la Donnée Brute aux Décisions Stratégiques

📝 Présentation du projet

NEXTBUY est un projet d'analyse de données massives portant sur des millions de commandes clients. L'objectif est de transformer ce volume de données en insights business actionnables pour améliorer les revenus, le marketing et l'efficacité opérationnelle d'une enseigne de grande distribution.

Objectifs remplis :

    Extraction de 8 insights business sous forme de questions/réponses.

    Prétraitement et nettoyage complet des datasets.

    Analyse exploratoire des données (EDA) avec graphiques avancés.

    Création et comparaison de modèles de Machine Learning (Random Forest, etc.).

    🚀 Installation et Configuration

Pour faire fonctionner ce projet sur votre machine, suivez les étapes ci-dessous :
1. Cloner le projet
git clone https://github.com/votre-username/B-DAT-201-nextbuy-3.git
cd B-DAT-201-nextbuy-3

2. Créer l'environnement virtuel

Il est fortement recommandé d'utiliser un environnement isolé pour éviter les conflits entre vos projets.
# Création de l'environnement
python -m venv .venv

# Activation (Linux/macOS)
source .venv/bin/activate

# Activation (Windows)
.venv\Scripts\activate

3. Installation des outils (Jupyter & Librairies)

Une fois l'environnement activé, installez les dépendances nécessaires :
pip install --upgrade pip
pip install jupyter pandas numpy matplotlib seaborn scikit-learn

📈 Utilisation de Jupyter Notebook

Le projet est entièrement contenu dans des fichiers .ipynb.
Via VS Code (Méthode recommandée)

    Ouvrez le dossier du projet dans VS Code.

    Installez l'extension "Jupyter" si ce n'est pas déjà fait.

    Ouvrez le fichier notebook.ipynb.

    En haut à droite, cliquez sur "Select Kernel" et choisissez votre environnement .venv.

    Cliquez sur "Run All" pour exécuter tout le code.

Via le navigateur

    Lancez le serveur dans votre terminal :
    jupyter notebook

    Dans l'interface qui s'ouvre, sélectionnez notebook.ipynb et exécutez les cellules.

📂 Aperçu de l'analyse

Le projet répond notamment aux questions suivantes :

    Top Produits : Quels sont les articles les plus vendus et les plus rachetés ?

    Comportement Horaire : À quelle heure les clients commandent-ils le plus en boulangerie ?

    Associations : Quels produits sont fréquemment achetés avec le chocolat ?

    Prédiction : Pouvons-nous prédire la taille du panier moyen (Score R2 obtenu : 0.58) ?

🛠️ Outils & Packages

    Python 3.x

    Pandas : Manipulation et nettoyage des données.

    Matplotlib & Seaborn : Visualisation de données (Graphiques en barres, lignes, nuages de points).

    Scikit-Learn : Algorithmes de Machine Learning (Random Forest Regressor).




from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# Cargar dataset
iris = load_iris()

X = iris.data      # características
y = iris.target    # etiquetas

# Dividir dataset en entrenamiento (70%) y prueba (30%)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Crear modelo de árbol de decisión
model = DecisionTreeClassifier()

# Entrenar modelo
model.fit(X_train, y_train)

# Predecir
y_pred = model.predict(X_test)

# Precisión
print("Accuracy:", accuracy_score(y_test, y_pred))

# Dibujar árbol de decisión
plt.figure(figsize=(10, 6))
tree.plot_tree(
    model,
    feature_names=iris.feature_names,
    class_names=iris.target_names,
    filled=True
)
plt.show()

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QMessageBox
from PyQt5.QtWidgets import QGridLayout, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import math
from errors import InvalidInputError, InvalidAValueError

class QuadraticEquation:

    def __init__(self, title ="Quaratic Equation", width = 900, height = 700):
        if not QApplication.instance():
            self.app = QApplication([])
            self.app.setStyleSheet("""
                QWidget {
                    text-align: center;
                    background-color: #F1F8E9; 
                    color: #333; 
                    font-size: 22px;
                    font-family: Poppins;
                    
                }

                QPushButton {
                    background-color: #4CAF50; 
                    color: white;
                    border-radius: 5px;
                    padding: 8px;
                }

                QPushButton:hover {
                    background-color: #388E3C; 
                }
                
                QPushButton:pressed {
                    background-color: #2E7D32;
                }
                
                QLineEdit {
                    background-color: white;
                    border: 2px solid #4CAF50;
                    color: #333;
                    border-radius: 5px;
                    padding: 5px;
                }                
                """)
        self.window = QWidget()
        self.title = title
        self.window.resize(width, height)
        self.window.setWindowTitle(self.title)

        self.a = None
        self.b = None
        self.c = None
        self.discriminant =  None
        self.result = []
        self.points = []
        self.symmetry_vertex = None
        
        self.grid_layout = QGridLayout()
        self.grid_layout.setHorizontalSpacing(5)  
        self.grid_layout.setVerticalSpacing(10) 
    
    def input_form(self):
        self.input_form_layout = QHBoxLayout()
        self.input_form_layout.setSpacing(10)
        self.input_form_layout.setContentsMargins(10,5,10,5)

        self.label_x_squared = QLabel("x² +")
        self.label_x = QLabel("x +")
        self.label_equal = QLabel(" = 0")
        
        self.x_squared = QLineEdit("")
        self.x_squared.setFixedSize(60,35)
        self.x_squared.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        self.x = QLineEdit("")
        self.x.setFixedSize(60,35)
        self.x.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        
        self.addition = QLineEdit("")
        self.addition.setFixedSize(60,35)
        self.addition.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        
        self.calculate_button = QPushButton("Calculate")
        self.calculate_button.setFixedSize(160,40)
        self.calculate_button.clicked.connect(self.run_app)

        self.input_form_layout.addWidget(self.x_squared)
        self.input_form_layout.addWidget(self.label_x_squared)
        self.input_form_layout.addWidget(self.x)
        self.input_form_layout.addWidget(self.label_x)
        self.input_form_layout.addWidget(self.addition)
        self.input_form_layout.addWidget(self.label_equal)
        self.input_form_layout.addWidget(self.calculate_button)
    
    def display_form(self):

        self.display_form_layout = QVBoxLayout()
        self.result_label = QLabel("Enter coefficients and press calculate.")
        self.display_form_layout.addWidget(self.result_label)
    
    def plot_form(self):
        self.figure = plt.figure()
        self.figure.set_facecolor("#F1F8E9")
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas,self.window)

        self.plot_form_layout = QVBoxLayout()
    
        self.plot_form_layout.addWidget(self.toolbar)
        self.plot_form_layout.addWidget(self.canvas)
    
    def layout(self):
        input_container = QWidget()
        input_container.setLayout(self.input_form_layout)
        input_container.setFixedSize(600, 80) 
        input_container.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)  # Büyüme engellendi
        self.grid_layout.addWidget(input_container, 1, 0, 1, 1, Qt.AlignLeft)

        self.grid_layout.addLayout(self.display_form_layout, 2, 0)
        self.grid_layout.addLayout(self.plot_form_layout,3,0,5,5)
        
    def reset_values(self):
        self.a = None
        self.b = None
        self.c = None
        self.result = []
        self.points = []
        self.symmetry_vertex = None
        self.discriminant = None
    
    def reset_input_values(self):
        self.x_squared.setText("")
        self.x.setText("") 
        self.addition.setText("") 
    
    def get_input(self):
        try:
            self.a = int(self.x_squared.text())
            self.b = int(self.x.text())
            self.c = int(self.addition.text())
        except:
            self.error_reset()
            raise InvalidInputError()
    
    def calculate_roots(self):
        
        if self.a != 0:
            self.discriminant = (self.b ** 2) - (4 * self.a* self.c)
            if self.discriminant > 0:
                root1 = (-self.b + math.sqrt(self.discriminant)) / (2 * self.a)  # First root
                root2 = (-self.b - math.sqrt(self.discriminant)) / (2 * self.a)  # Second root
                self.result.append(root1)
                self.result.append(root2)
                
            elif self.discriminant == 0:
                # One real root (roots are equal)
                root = -self.b / (2 * self.a)  # Single root
                self.result.append(root)
            else:
                self.result = []
        else:
            self.error_reset()
            raise InvalidAValueError()
       
    
    def calculate_equation(self, value):
            return (self.a * value ** 2) + (self.b * value) + (self.c)
    
    def calculate_visual_vertices(self):
        if self.discriminant:
            self.symmetry_vertex = (self.b * -1) / (self.a * 2)
            sub_value = 20
            for i in range(0,41):
                x = self.symmetry_vertex - sub_value
                self.points.append((x, self.calculate_equation(x)))
                sub_value -= 1
         
    def display(self):
        discr_text = f"📌 Discriminant: {self.discriminant:.2f}\n"
        
        if self.discriminant > 0:
            root_text = f"✅ The equation has 2 real roots:\n   ➤ Root 1: {self.result[0]:.4f}\n   ➤ Root 2: {self.result[1]:.4f}"
        elif self.discriminant == 0:
            root_text = f"✅ The equation has 1 real root:\n   ➤ Root: {self.result[0]:.4f}"
        else:
            root_text = "❌ No real roots exist (Complex numbers)."

        self.result_label.setText(discr_text + root_text)

    def plot(self):
        plt.rcParams.update({'font.size': 16})
        if self.discriminant is not None:
            x_values, y_values = zip(*self.points)

            self.figure.clear()
            ax = self.figure.add_subplot(111)

            ax.plot(x_values, y_values, color="#390d6e", label="Quadratic Curve")
            ax.axhline(0, color="black", linestyle="--", linewidth=1.5, label="X-axis")  # X-axis
            ax.axvline(0, color="black", linestyle="--", linewidth=1.5, label="Y-axis")  # Y-axis
            if self.discriminant >= 0:
                ax.scatter(self.result, [0] * len(self.result), color="#FF9800", marker="o", s=80, label="Roots")
            ax.legend()
            ax.grid(True, linestyle="--", alpha=0.6)
            self.figure.suptitle("The Roots and Graph of a Quadratic Equation.", fontsize = 20, weight = "bold", color = "#333")
            self.canvas.draw()
        
    def reset_plot(self):
        self.figure.clf()
        self.canvas.draw()
       
    def error_reset(self):
        self.reset_values()
        self.reset_input_values()
        self.reset_plot()
    
    def run_functions_in_order(self, *methods): 
        for method in methods:
            try:
                method()
            except Exception as e:
                print(f"Error in {method.__name__}: {e}")  
                break  

    def run_app(self):
        self.run_functions_in_order(self.reset_values,self.get_input, self.calculate_roots, self.calculate_visual_vertices, self.display, self.plot)


if __name__ == "__main__":

    app = QuadraticEquation()
    app.window.setLayout(app.grid_layout)
    app.input_form()
    app.display_form()
    app.plot_form()
    app.layout()
    app.window.show()
    app.app.exec_()
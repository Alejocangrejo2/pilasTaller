from evaluator import ExpressionEvaluator

def autocorrect_parentheses(expr):
    """Corrige automáticamente paréntesis desbalanceados"""
    open_count = 0
    corrected = ""
    
    for char in expr:
        if char == "(":
            open_count += 1
            corrected += char
        elif char == ")":
            if open_count > 0:
                open_count -= 1
                corrected += char
            else:
                # Paréntesis de cierre extra → ignorar
                continue
        else:
            corrected += char
    
    # Si faltan cierres al final, agregarlos
    corrected += ")" * open_count
    return corrected

if __name__ == "__main__":
    while True:
        expr = input("\nIngresa la expresión matemática (o 'salir' para terminar): ")
        if expr.lower() == "salir":
            print("Saliendo...")
            break

        while True:
            print("\nExpresión actual:", expr)
            print("Opciones:")
            print("1. Corregir paréntesis automáticamente")
            print("2. Comprobar/Calcular expresión")
            print("3. Ingresar nueva expresión")
            opcion = input("Elige opción (1-3): ")

            if opcion == "1":
                expr_corregida = autocorrect_parentheses(expr)
                if expr != expr_corregida:
                    print(f"Expresión corregida automáticamente a: {expr_corregida}")
                    expr = expr_corregida
                else:
                    print("La expresión ya está balanceada.")
            elif opcion == "2":
                try:
                    evaluator = ExpressionEvaluator(expr)
                    resultado = evaluator.evaluate()
                    print(f"Resultado: {resultado}")
                except Exception as e:
                    print(f"Error: {e}")
            elif opcion == "3":
                break
            else:
                print("Opción inválida, intenta de nuevo.")

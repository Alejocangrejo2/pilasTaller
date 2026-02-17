from stack import Stack

class ExpressionEvaluator:
    def __init__(self, expression):
        self.expression = expression.replace(" ", "")

    # Validar paréntesis
    def validate_parentheses(self):
        stack = Stack()
        for char in self.expression:
            if char == "(":
                stack.push(char)
            elif char == ")":
                if stack.is_empty():
                    return False
                stack.pop()
        return stack.is_empty()

    # Precedencia
    def precedence(self, operator):
        if operator in ("+", "-"):
            return 1
        if operator in ("*", "/"):
            return 2
        return 0

    # Convertir infijo a postfijo
    def infix_to_postfix(self):
        stack = Stack()
        output = []
        number = ""

        for char in self.expression:
            if char.isdigit():
                number += char
            else:
                if number:
                    output.append(number)
                    number = ""

                if char == "(":
                    stack.push(char)
                elif char == ")":
                    while not stack.is_empty() and stack.peek() != "(":
                        output.append(stack.pop())
                    if stack.is_empty():
                        raise ValueError("Paréntesis desbalanceados")
                    stack.pop()
                elif char in "+-*/":
                    while (not stack.is_empty() and
                           self.precedence(stack.peek()) >= self.precedence(char)):
                        output.append(stack.pop())
                    stack.push(char)

        if number:
            output.append(number)

        while not stack.is_empty():
            top = stack.pop()
            if top in "()":
                raise ValueError("Paréntesis desbalanceados")
            output.append(top)

        return output

    # Evaluar postfijo
    def evaluate_postfix(self, postfix):
        stack = Stack()
        for token in postfix:
            if token.isdigit():
                stack.push(int(token))
            else:
                b = stack.pop()
                a = stack.pop()
                if a is None or b is None:
                    raise ValueError("Expresión inválida")
                if token == "+":
                    stack.push(a + b)
                elif token == "-":
                    stack.push(a - b)
                elif token == "*":
                    stack.push(a * b)
                elif token == "/":
                    if b == 0:
                        raise ZeroDivisionError("División por cero")
                    stack.push(a / b)
        if stack.size() != 1:
            raise ValueError("Expresión inválida")
        return stack.pop()

    # Método principal
    def evaluate(self):
        if not self.validate_parentheses():
            raise ValueError("Paréntesis no balanceados")
        postfix = self.infix_to_postfix()
        return self.evaluate_postfix(postfix)

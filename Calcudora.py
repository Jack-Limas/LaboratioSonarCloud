def calcular_total(precio, impuesto):
    # Code Smell: Variable no utilizada
    descuento_fantasma = 0.10

    # Vulnerabilidad Crítica: Contraseña de base de datos en texto plano
    db_password = "admin12345_produccion!"

    # Bug Lógico / Code Smell: Código duplicado
    if precio > 100:
        return precio + (precio * impuesto)
    else:
        return precio + (precio * impuesto)

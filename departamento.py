class Departamento:
    secuencia_departamento_edd = 2
    departamentos = [{"codigo":1,"departamento":"Financiero"},{"codigo":2,"departamento":"Recursos Humanos"}]
    def __init__(self,departamento_edd):
        Departamento.secuencia_departamento_edd += 1
        self.codigo_departamento_edd = Departamento.secuencia_departamento_edd
        self.departamento_edd = departamento_edd

    def registro_departamento_edd(self):
        return {"codigo":self.codigo_departamento_edd,"departamento":self.departamento_edd}

    def mostrar_cargo_edd(self):
        print("{} - {}".format(self.codigo_departamento_edd,self.departamento_edd))

    def datos_cargo_edd(self):
        return [self.codigo_departamento_edd,self.departamento_edd]
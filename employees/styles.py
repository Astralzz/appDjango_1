# SECTION - Estilo
class Style:
    # STUB - Clases
    class ClassStyle:
        """_get_default_input_

        Estilo para los inputs
        
        Parameters:
             extra_style (str, optional): _Estilos extras_. Defaults to "".

        Returns:
            _type_: _string_
        """

        @staticmethod
        def get_default_input(extra_style = ""):
            return "form-control mb-3 " + str(extra_style)

        """_get_select_input_

        Estilo para los inputs select
        
        Parameters:
             extra_style (str, optional): _Estilos extras_. Defaults to "".

        Returns:
            _type_: _string_
        """

        @staticmethod
        def get_select_input(extra_style = ""):
            return "form-select mb-3 " + str(extra_style)


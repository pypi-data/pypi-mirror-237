class Cell:
    def __init__(self, data_frame, row, col):
        self.row = row
        self.col = col
        self.data_frame = data_frame
        self.content = self.data_frame.iloc[row, col]
        self.input_dict = {
            "Text": "type='text'",
            "Password": "type='password'",
            "Date": "type='date'",
            "File": "type=file",
            "Submit": "type='submit'",
            "Email": "type='email'"
        }
        self.complex_input_list = ["Dropdown", "Checkbox", "Radio"]

    def get_html(self):
        """Matches the input into the corresponding input dictionary

        Returns:
            String: HTML attribute
        """
        isComplex = self.check_if_complex_input()
        if self.content in self.input_dict.keys():
            return self.create_input()
        elif str(self.content) == 'nan':
            return ""
        elif isComplex[0]:
            return self.create_complex_input(isComplex[1], isComplex[2])
        else:
            return f"<label for='{self.content}' name='{self.content}'>{self.content}</label>"

    def create_input(self):
        """Gives the corresponding HTML input string

        Returns:
            String: HTML input
        """
        top = self.data_frame.iloc[self.row - 1, self.col]
        left = self.data_frame.iloc[self.row, self.col - 1]

        if left in self.input_dict.keys() or str(left) == 'nan':
            if top in self.input_dict.keys() or str(top) == 'nan':
                return f"<input {self.input_dict[self.content]}/>"
            else:
                return f"<input id='{top}' {self.input_dict[self.content]}/>"
        else:
            return f"<input id='{left}' {self.input_dict[self.content]}/>"

    def check_if_complex_input(self):
        """Checks if the given content is a complex_input

        Returns:
            Tuple: (Boolean, Any, Any) Returns the complex_input as a tuple
        """
        input_split = str(self.content).split(":")
        if input_split[0] in self.complex_input_list:
            return (True, input_split[0], input_split[1])
        return (False, None, None)

    def create_complex_input(self, complex_input_type, complex_input_contents):
        """Creates a complex_input given the type and contents

        Args:
            complex_input_type (String): Type of complex input
            complex_input_contents (String): Contents of complex input

        Returns:
            String: HTML representation of the complex input
        """
        match complex_input_type:
            case "Checkbox":
                return self.create_checkbox_input(complex_input_contents)
            case "Radio":
                return self.create_radio_input(complex_input_contents)
            case "Dropdown":
                return self.create_dropdown_input(complex_input_contents)

    def create_checkbox_input(self, contents):
        """Creates the HTML representation of the contents as a checkbox input

        Args:
            contents (String): String representation of the contents in the checkbox

        Returns:
            String: HTML representation of the checkbox
        """
        contentsList = contents.split(",")
        checkbox_html = f"<fieldset><legend>{contentsList[0]}</legend>"
        for i in range(1, len(contentsList)):
            label = "<div>"
            label += f"<input type='checkbox' id={contentsList[i]} name={contentsList[i]}/>"
            label += f"<label for={contentsList[i]}>{contentsList[i]}</label>"
            label += "</div>"
            checkbox_html += label
        checkbox_html += "</fieldset>"
        return checkbox_html

    def create_radio_input(self, contents):
        """Creates the HTMl representation of the contents as a radio input

        Args:
            contents (String): String representation of the contents in the radio

        Returns:
            String: HTML representation of the radio input
        """
        contentsList = contents.split(",")
        radio_html = f"<fieldset><legend>{contentsList[0]}</legend>"
        for i in range(1, len(contentsList)):
            label = "<div>"
            label += f"<input type='radio' id={contentsList[i]} name={contentsList[0]} value={contentsList[i]}/>"
            label += f"<label for={contentsList[i]}>{contentsList[i]}</label>"
            label += "</div>"
            radio_html += label
        radio_html += "</fieldset>"
        return radio_html

    def create_dropdown_input(self, contents):
        """Creates the HTMl representation of the contents as a dropdown input

        Args:
            contents (String): String representation of the contents in the dropdown

        Returns:
            String: HTML representation of the dropdown input
        """
        contentsList = contents.split(",")
        dropdown_html = f"<fieldset><label for={contentsList[0]}>{contentsList[0]}:</label><select name={contentsList[0]} id={contentsList[0]}>"
        for i in range(1, len(contentsList)):
            dropdown_html += f"<option value={contentsList[i]}>{contentsList[i]}</option>"
        dropdown_html += "</select></fieldset>"
        return dropdown_html

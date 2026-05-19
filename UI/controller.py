import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._ddInsValue = None

    def handle_btn_cerca_iscritti(self, e):
        """Simple function to handle a button-pressed event,
        and consequently print a message on screen"""

        self._view.txt_result.controls.clear()

        if self._ddInsValue is None:
            self._view.create_alert("Per favore selezionare un insegnamento.")
            self._view.update_page()
            return


        studenti = self._model.getIscrittiCorso(self._ddInsValue.codins)
        if not len(studenti):
            self._view.txt_result.controls.append(ft.Text(f"Nessuno studente è iscritto al corso {self._ddInsValue}"))
            return

        self._view.txt_result.controls.append(ft.Text(f"Di seguito gli iscritti al corso {self._ddInsValue}!"))
        self._view.update_page()

        for s in studenti:
            self._view.txt_result.controls.append(ft.Text(s))
            self._view.update_page()

    def fill_ddCDS(self):
        for corso in self._model.getAllCorsi():
            self._view._ddCDS.options.append(ft.dropdown.Option(
                key = corso.codins,
                text = corso.__str__(),
                data = corso,
                on_click = self._choiceDDCodins
            ))
            pass

    def _choiceDDCodins(self, e):
        self._ddInsValue = e.control.data
        print(self._ddInsValue)
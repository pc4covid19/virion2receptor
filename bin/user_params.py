 
# This file is auto-generated from a Python script that parses a PhysiCell configuration (.xml) file.
#
# Edit at your own risk.
#
import os
from ipywidgets import Label,Text,Checkbox,Button,HBox,VBox,FloatText,IntText,BoundedIntText,BoundedFloatText,Layout,Box
    
class UserTab(object):

    def __init__(self):
        
        micron_units = Label('micron')   # use "option m" (Mac, for micro symbol)

        constWidth = '180px'
        tab_height = '500px'
        stepsize = 10

        #style = {'description_width': '250px'}
        style = {'description_width': '25%'}
        layout = {'width': '400px'}

        name_button_layout={'width':'25%'}
        widget_layout = {'width': '15%'}
        units_button_layout ={'width':'15%'}
        desc_button_layout={'width':'45%'}
        divider_button_layout={'width':'40%'}

        param_name1 = Button(description='random_seed', disabled=True, layout=name_button_layout)
        param_name1.style.button_color = 'lightgreen'

        self.random_seed = IntText(
          value=0,
          step=1,
          style=style, layout=widget_layout)

        div_row1 = Button(description='---Virus Adsorption and Export---', disabled=True, layout=divider_button_layout)

        param_name2 = Button(description='virion_export_rate', disabled=True, layout=name_button_layout)
        param_name2.style.button_color = 'tan'

        self.virion_export_rate = FloatText(
          value=0.01,
          step=0.001,
          style=style, layout=widget_layout)

        div_row2 = Button(description='---ACE2 receptor dynamics with virus binding---', disabled=True, layout=divider_button_layout)

        param_name3 = Button(description='ACE2_receptors_per_cell', disabled=True, layout=name_button_layout)
        param_name3.style.button_color = 'lightgreen'

        self.ACE2_receptors_per_cell = FloatText(
          value=1000,
          step=100,
          style=style, layout=widget_layout)

        param_name4 = Button(description='ACE2_binding_rate', disabled=True, layout=name_button_layout)
        param_name4.style.button_color = 'tan'

        self.ACE2_binding_rate = FloatText(
          value=0.001,
          step=0.0001,
          style=style, layout=widget_layout)

        param_name5 = Button(description='ACE2_endocytosis_rate', disabled=True, layout=name_button_layout)
        param_name5.style.button_color = 'lightgreen'

        self.ACE2_endocytosis_rate = FloatText(
          value=0.01,
          step=0.001,
          style=style, layout=widget_layout)

        param_name6 = Button(description='ACE2_cargo_release_rate', disabled=True, layout=name_button_layout)
        param_name6.style.button_color = 'tan'

        self.ACE2_cargo_release_rate = FloatText(
          value=0.001,
          step=0.0001,
          style=style, layout=widget_layout)

        param_name7 = Button(description='ACE2_recycling_rate', disabled=True, layout=name_button_layout)
        param_name7.style.button_color = 'lightgreen'

        self.ACE2_recycling_rate = FloatText(
          value=0.01,
          step=0.001,
          style=style, layout=widget_layout)

        div_row3 = Button(description='---Initialization Options--', disabled=True, layout=divider_button_layout)

        param_name8 = Button(description='multiplicity_of_infection', disabled=True, layout=name_button_layout)
        param_name8.style.button_color = 'tan'

        self.multiplicity_of_infection = FloatText(
          value=0.01,
          step=0.001,
          style=style, layout=widget_layout)

        param_name9 = Button(description='use_single_infected_cell', disabled=True, layout=name_button_layout)
        param_name9.style.button_color = 'lightgreen'

        self.use_single_infected_cell = Checkbox(
          value=False,
          style=style, layout=widget_layout)

        div_row4 = Button(description='---Visualization Options---', disabled=True, layout=divider_button_layout)

        param_name10 = Button(description='color_variable', disabled=True, layout=name_button_layout)
        param_name10.style.button_color = 'tan'

        self.color_variable = Text(
          value='virion',
          style=style, layout=widget_layout)

        units_button1 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button1.style.button_color = 'lightgreen'
        units_button2 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button2.style.button_color = 'lightgreen'
        units_button3 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button3.style.button_color = 'tan'
        units_button4 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button4.style.button_color = 'tan'
        units_button5 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button5.style.button_color = 'lightgreen'
        units_button6 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button6.style.button_color = 'tan'
        units_button7 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button7.style.button_color = 'lightgreen'
        units_button8 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button8.style.button_color = 'tan'
        units_button9 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button9.style.button_color = 'lightgreen'
        units_button10 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button10.style.button_color = 'lightgreen'
        units_button11 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button11.style.button_color = 'tan'
        units_button12 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button12.style.button_color = 'lightgreen'
        units_button13 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button13.style.button_color = 'lightgreen'
        units_button14 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button14.style.button_color = 'tan'

        desc_button1 = Button(description='' , tooltip='', disabled=True, layout=desc_button_layout) 
        desc_button1.style.button_color = 'lightgreen'
        desc_button6 = Button(description='rate at which a virion is exported from a live cell' , tooltip='rate at which a virion is exported from a live cell', disabled=True, layout=desc_button_layout) 
        desc_button6.style.button_color = 'tan'
        desc_button7 = Button(description='number of ACE2 receptors per cell' , tooltip='number of ACE2 receptors per cell', disabled=True, layout=desc_button_layout) 
        desc_button7.style.button_color = 'lightgreen'
        desc_button8 = Button(description='ACE2 receptor-virus binding rate' , tooltip='ACE2 receptor-virus binding rate', disabled=True, layout=desc_button_layout) 
        desc_button8.style.button_color = 'tan'
        desc_button9 = Button(description='ACE2 receptor-virus endocytosis rate' , tooltip='ACE2 receptor-virus endocytosis rate', disabled=True, layout=desc_button_layout) 
        desc_button9.style.button_color = 'lightgreen'
        desc_button10 = Button(description='ACE2 receptor-virus cargo release rate' , tooltip='ACE2 receptor-virus cargo release rate', disabled=True, layout=desc_button_layout) 
        desc_button10.style.button_color = 'tan'
        desc_button11 = Button(description='ACE2 receptor recycling rate' , tooltip='ACE2 receptor recycling rate', disabled=True, layout=desc_button_layout) 
        desc_button11.style.button_color = 'lightgreen'
        desc_button16 = Button(description='multiplicity of infection: virions/cells at t=0' , tooltip='multiplicity of infection: virions/cells at t=0', disabled=True, layout=desc_button_layout) 
        desc_button16.style.button_color = 'tan'
        desc_button17 = Button(description='Infect center cell with one virion (overrides MOI)' , tooltip='Infect center cell with one virion (overrides MOI)', disabled=True, layout=desc_button_layout) 
        desc_button17.style.button_color = 'lightgreen'
        desc_button18 = Button(description='color cells based on this variable' , tooltip='color cells based on this variable', disabled=True, layout=desc_button_layout) 
        desc_button18.style.button_color = 'tan'

        row1 = [param_name1, self.random_seed, units_button1, desc_button1] 
        row6 = [param_name2, self.virion_export_rate, units_button3, desc_button6] 
        row7 = [param_name3, self.ACE2_receptors_per_cell, units_button5, desc_button7] 
        row8 = [param_name4, self.ACE2_binding_rate, units_button6, desc_button8] 
        row9 = [param_name5, self.ACE2_endocytosis_rate, units_button7, desc_button9] 
        row10 = [param_name6, self.ACE2_cargo_release_rate, units_button8, desc_button10] 
        row11 = [param_name7, self.ACE2_recycling_rate, units_button9, desc_button11] 
        row16 = [param_name8, self.multiplicity_of_infection, units_button11, desc_button16] 
        row17 = [param_name9, self.use_single_infected_cell, units_button12, desc_button17] 
        row18 = [param_name10, self.color_variable, units_button14, desc_button18] 

        box_layout = Layout(display='flex', flex_flow='row', align_items='stretch', width='100%')
        box1 = Box(children=row1, layout=box_layout)
        box6 = Box(children=row6, layout=box_layout)
        box7 = Box(children=row7, layout=box_layout)
        box8 = Box(children=row8, layout=box_layout)
        box9 = Box(children=row9, layout=box_layout)
        box10 = Box(children=row10, layout=box_layout)
        box11 = Box(children=row11, layout=box_layout)
        box16 = Box(children=row16, layout=box_layout)
        box17 = Box(children=row17, layout=box_layout)
        box18 = Box(children=row18, layout=box_layout)

        self.tab = VBox([
          box1,
          div_row1,
          box6,
          div_row2,
          box7,
          box8,
          box9,
          box10,
          box11,
          div_row3,
          box16,
          box17,
          div_row4,
          box18,
        ])

    # Populate the GUI widgets with values from the XML
    def fill_gui(self, xml_root):
        uep = xml_root.find('.//microenvironment_setup')  # find unique entry point
        vp = []   # pointers to <variable> nodes
        if uep:
            for var in uep.findall('variable'):
                vp.append(var)

        uep = xml_root.find('.//user_parameters')  # find unique entry point
        self.random_seed.value = int(uep.find('.//random_seed').text)
        self.virion_export_rate.value = float(uep.find('.//virion_export_rate').text)
        self.ACE2_receptors_per_cell.value = float(uep.find('.//ACE2_receptors_per_cell').text)
        self.ACE2_binding_rate.value = float(uep.find('.//ACE2_binding_rate').text)
        self.ACE2_endocytosis_rate.value = float(uep.find('.//ACE2_endocytosis_rate').text)
        self.ACE2_cargo_release_rate.value = float(uep.find('.//ACE2_cargo_release_rate').text)
        self.ACE2_recycling_rate.value = float(uep.find('.//ACE2_recycling_rate').text)
        self.multiplicity_of_infection.value = float(uep.find('.//multiplicity_of_infection').text)
        self.use_single_infected_cell.value = ('true' == (uep.find('.//use_single_infected_cell').text.lower()) )
        self.color_variable.value = (uep.find('.//color_variable').text)


    # Read values from the GUI widgets to enable editing XML
    def fill_xml(self, xml_root):
        uep = xml_root.find('.//microenvironment_setup')  # find unique entry point
        vp = []   # pointers to <variable> nodes
        if uep:
            for var in uep.findall('variable'):
                vp.append(var)

        uep = xml_root.find('.//user_parameters')  # find unique entry point
        uep.find('.//random_seed').text = str(self.random_seed.value)
        uep.find('.//virion_export_rate').text = str(self.virion_export_rate.value)
        uep.find('.//ACE2_receptors_per_cell').text = str(self.ACE2_receptors_per_cell.value)
        uep.find('.//ACE2_binding_rate').text = str(self.ACE2_binding_rate.value)
        uep.find('.//ACE2_endocytosis_rate').text = str(self.ACE2_endocytosis_rate.value)
        uep.find('.//ACE2_cargo_release_rate').text = str(self.ACE2_cargo_release_rate.value)
        uep.find('.//ACE2_recycling_rate').text = str(self.ACE2_recycling_rate.value)
        uep.find('.//multiplicity_of_infection').text = str(self.multiplicity_of_infection.value)
        uep.find('.//use_single_infected_cell').text = str(self.use_single_infected_cell.value)
        uep.find('.//color_variable').text = str(self.color_variable.value)

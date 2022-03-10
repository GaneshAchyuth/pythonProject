class Car:
    def __init__(self,engine_type,fuel_type):
        self.engine_type = engine_type
        self.fuel_type = fuel_type

    def print_engine_type(variable_engine_type):
        print(variable_engine_type)

   tesla = Car(engine_type='electric_motor',fuel_type='electricity')
   swift = Car(engine_type= 'petrol_motor_v4',fuel_type='petrol')
   fortuner = Car(engine_type='disel_motor_v8',fuel_type='disel')
   Car.print_engine_type(tesla.engine_type)




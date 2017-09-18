import json
class ExtraString(dict):

    def classify(self):
        with open('../config.json') as json_data:
            d = json.load(json_data)
        for key,value in self.items():
            maximo = int (d[key]['maximo'])
            minimo = int (d[key]['minimo'])
            valor = int(value)
            if (minimo > valor or valor > maximo):
                return False
        return True

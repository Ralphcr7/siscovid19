from flask import Flask, render_template, request, jsonify #Importar libreria Flask y render_template para renderizar archivos HTMl
import json
from products import products
app = Flask(__name__)

@app.route('/products', methods=['GET'])
def getDatos():
    with open('prueba.json') as json_file:
        Datos = json.load(json_file)
    return jsonify ({"products": Datos,",message":"Lista de datos guardados"})

#######agrega un nuevo prodcuto#########   
@app.route('/sendproducts',methods=['POST']) #Enviar datos al JSON
def addProduct():
    new_product = {
        "name":request.json['name'],
        "apellido" : request.json['apellido'],
        "edad" : request.json['edad']
    }
    products.append(new_product)
    with open('prueba.json', 'w') as json_file:
        json.dump(products, json_file)    
    return jsonify({"message": "product added sussefuly","products":products})


@app.route('/products/<string:product_name>',methods=['GET'])
def getProduct(product_name):
    resultado = "null"
    with open('prueba.json') as json_file:
        data = json.load(json_file)
        
        for item in data:
                
            if(item['name']==product_name):
                resultado =  [
                {   "name" : item['name'],
                    "apellido" : item['apellido'],
                    "edad" : item['edad']
                } ,
                
                ]
    if(resultado=="null"):
        return jsonify({"message": "product not found"})
    else:
        return jsonify({"products": resultado,",message":"Lista de productos"})
     


@app.route('/products/<string:product_name>',methods=['DELETE'])
def deleteProduc(product_name):
    product_found=[product for product in products if product['name']==product_name ]
    if(len(product_found)>0):
        products.remove(product_found[0])
        return jsonify({"message": "product delete sussefuly","products":products})
    return jsonify({"message": "product not found"})



@app.route('/products/<string:product_name>',methods=['PUT'])
def editProduct(product_name):
    product_found=[product for product in products if product['name']==product_name ]
    if(len(product_found)>0):
        product_found[0]['name']=request.json['name']
        product_found[0]['apellido']=request.json['apellido']
        product_found[0]['edad']=request.json['edad']
        return jsonify({"message": "product update sussefuly","products":products})
    return jsonify({"message": "product not found"})



#######################################################################################

if __name__ == '__main__':
    app.run(port = 4000, debug = True)
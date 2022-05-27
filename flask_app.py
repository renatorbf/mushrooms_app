from flask import Flask, render_template, request

from helper_nb import run_model

import sys

#Flask Logic 

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    
    if request.method == 'POST':
        #do the logic of retriving the inputs from the user in the web app
        
        cap_shape = request.form['cap-shape']
        cap_surface = request.form['cap-surface']
        cap_color = request.form['cap-color']
        bruises = request.form['bruises']
        odor = request.form['odor']
        gill_attachment = request.form['gill-attachment']
        gill_spacing = request.form['gill-spacing']
        gill_size = request.form['gill-size']
        gill_color = request.form['gill-color']
        gilstalk_shape = request.form['stalk-shape']
        stalk_root = request.form['stalk-root']
        stalk_surface_above_ring = request.form['stalk-surface-above-ring']
        stalk_surface_below_ring = request.form['stalk-surface-below-ring']
        stalk_color_above_ring = request.form['stalk-color-above-ring']
        stalk_color_below_ring = request.form['stalk-color-below-ring']
        veil_type = request.form['veil-type']
        veil_color = request.form['veil-color']
        ring_number = request.form['ring-number']
        ring_type = request.form['ring-type']
        spore_print_color = request.form['spore-print-color']
        population = request.form['population']
        habitat = request.form['habitat']
        
        list_features = [cap_shape, cap_surface, cap_color, bruises, odor, gill_attachment, gill_spacing, gill_size, gill_color, gilstalk_shape, stalk_root, stalk_surface_above_ring, stalk_surface_below_ring, stalk_color_above_ring,stalk_color_below_ring, veil_type, veil_color, ring_number, ring_type, spore_print_color, population, habitat]
        
        # prediction = run_model(list_features)
        print(list_features)
        prediction = run_model(list_features)
        # print('I got this, cap shape: ' + cap_shape)
        
        # print(type(prediction), file = sys.stderr)
        print('I am doing some tests')
        
        if prediction == 0:
            name = 'Poisonous'
        else:
            name = 'Edible'
        
        # return render_template('main.html')
        # return render_template('main.html', results = name)
        extra = 'This is '
        return render_template('main.html', extra = extra, results = name)
    
    else:
        return render_template('main.html')




if __name__ == "__main__":
    app.run(debug= False, port = 3012, host="0.0.0.0")
    # app.run(debug= False, port = 3012, host="0.0.0.0") # this line makes the app run only locally
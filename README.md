# lhcbMLbets

The notebooks here are personal notes derived from various sources, even from outside LHCb. 
Previous work are found in the Resources/References section below.


# Tips 
## Converting python to ipynb 
```
pip install p2j
p2j myscript.pyt
```

## Mitigating problems with google colab

* Keep console alive through script that stimulates clicking
```
function clickButton() {
    document.querySelectorAll('colab-toolbar-button')[2].click();
}
setInterval(clickButton, 60000); // Clicks every minute
```

* Save and load checkpoints
```
import tensorflow as tf

checkpoint_callback = tf.keras.callbacks.ModelCheckpoint(
    'path_to_save_model/model_checkpoint.h5',
    save_best_only=True
)

model.fit(
    x_train, y_train,
    epochs=10,
    callbacks=[checkpoint_callback]
)

# Reload the model 
model = tf.keras.models.load_model('path_to_save_model/model_checkpoint.h5')
```

# Python environment

``````
# Create a virtual environment
python -m venv myenv

# Activate the virtual environment
source myenv/bin/activate  # For macOS/Linux
# myenv\Scripts\activate  # For Windows

# Install required packages
pip install pandas h5py pyarrow
``````


# Resources and References 

## Electron vs Photon
* Original Paper: [M Andrews et al 2018J. Phys.: Conf. Ser. 1085 042022](https://iopscience.iop.org/article/10.1088/1742-6596/1085/4/042022/pdf)
* [Summer Student Report](https://cds.cern.ch/record/2824815/files/Final%20Report%20-%20Fahed%20AlRashidi.pdf)
* [CMU Poster](https://www.cmu.edu/ai-physics-institute/outreach/surp/images/2022/manami-kanemura-poster.pdf)
* [Gentle Introduction to Machine Learning for Particle Physics](https://github.com/Manami-16/Intro_to_Deep_Learning_for_Particle_Physics)
* [KyungMinPark Github](https://github.com/kyungminparkdrums/EGamma/blob/master/EGamma_ML.ipynb)

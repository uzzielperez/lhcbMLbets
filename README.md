# lhcbMLbets

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

# Resources 

* [Summer Student Report](https://cds.cern.ch/record/2824815/files/Final%20Report%20-%20Fahed%20AlRashidi.pdf)
* [CMU Poster](https://www.cmu.edu/ai-physics-institute/outreach/surp/images/2022/manami-kanemura-poster.pdf)
* [Gentle Introduction to Machine Learning for Particle Physics](https://github.com/Manami-16/Intro_to_Deep_Learning_for_Particle_Physics)
* [KyungMinPark Github](https://github.com/kyungminparkdrums/EGamma/blob/master/EGamma_ML.ipynb)
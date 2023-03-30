import tensorflow as tf
from keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import EarlyStopping

train_datagen = ImageDataGenerator(rescale=1. / 255)

train_generator = train_datagen.flow_from_directory(
    'PhoneRealDataset',
    target_size=(224, 224),
    batch_size=32,
    class_mode='binary',
    classes=['real', 'fake'])

model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(128, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(128, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])
model.compile(loss='binary_crossentropy',
              optimizer=tf.keras.optimizers.RMSprop(),
              metrics=['accuracy'])
earlystop_callback = EarlyStopping(
    monitor='accuracy',  # the quantity to be monitored
    min_delta=0.01,  # minimum change in the monitored quantity to qualify as an improvement
    patience=3,  # number of epochs with no improvement after which training will be stopped
    verbose=1,  # verbosity mode
    restore_best_weights=True  # restore the weights from the epoch with the best monitored quantity
)
history = model.fit(
    train_generator,
    steps_per_epoch=train_generator.samples / train_generator.batch_size,
    epochs=10,
    verbose=1,
    callbacks=[earlystop_callback])
model.save('classifier.h5')
# EVALUATE
test_datagen = ImageDataGenerator(rescale=1. / 255)

test_generator = test_datagen.flow_from_directory(
    'TestSet',
    target_size=(224, 224),
    batch_size=32,
    class_mode='binary',
    classes=['real', 'fake'])

test_loss, test_acc = model.evaluate(test_generator, verbose=1)
print('Test accuracy:', test_acc)

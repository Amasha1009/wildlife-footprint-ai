import tensorflow as tf

# Dataset paths
TRAIN_DIR = "dataset/split/train"
VALIDATION_DIR = "dataset/split/validation"
TEST_DIR = "dataset/split/test"

# Image settings
IMG_SIZE = (224, 224)
BATCH_SIZE = 8

# Load training dataset
train_dataset = tf.keras.utils.image_dataset_from_directory(
    TRAIN_DIR,
    image_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    shuffle=True
)

# Load validation dataset
validation_dataset = tf.keras.utils.image_dataset_from_directory(
    VALIDATION_DIR,
    image_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    shuffle=False
)

# Load test dataset
test_dataset = tf.keras.utils.image_dataset_from_directory(
    TEST_DIR,
    image_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    shuffle=False
)

# Display detected classes
print("Classes:", train_dataset.class_names)

print("Training dataset loaded successfully.")
print("Validation dataset loaded successfully.")
print("Test dataset loaded successfully.")


# Load pre-trained MobileNetV3Small
base_model = tf.keras.applications.MobileNetV3Small(
    input_shape=(224, 224, 3),
    include_top=False,
    weights="imagenet"
)

# Freeze the pre-trained layers
base_model.trainable = False

print("MobileNetV3Small loaded successfully.")

# Add classification layers
inputs = tf.keras.Input(shape=(224, 224, 3))

x = base_model(inputs, training=False)
x = tf.keras.layers.GlobalAveragePooling2D()(x)
x = tf.keras.layers.Dropout(0.2)(x)

outputs = tf.keras.layers.Dense(
    6,
    activation="softmax"
)(x)

model = tf.keras.Model(inputs, outputs)

print("6-class wildlife model created successfully.")

# Compile the model
model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.0001),
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

print("Model compiled successfully.")

# Training callbacks
early_stopping = tf.keras.callbacks.EarlyStopping(
    monitor="val_loss",
    patience=5,
    restore_best_weights=True
)

model_checkpoint = tf.keras.callbacks.ModelCheckpoint(
    "model/best_wildlife_model.keras",
    monitor="val_accuracy",
    save_best_only=True
)

print("Training callbacks configured successfully.")

# Train the model
print("Starting model training...")

history = model.fit(
    train_dataset,
    validation_data=validation_dataset,
    epochs=20,
    callbacks=[early_stopping, model_checkpoint]
)

print("Model training completed successfully.")

# Evaluate the model on the test dataset
print("Evaluating model on test dataset...")

test_loss, test_accuracy = model.evaluate(test_dataset)

print(f"Test Loss: {test_loss:.4f}")
print(f"Test Accuracy: {test_accuracy:.4f}")

# Save the final trained model
model.save("model/wildlife_model.keras")

print("Final model saved successfully.")
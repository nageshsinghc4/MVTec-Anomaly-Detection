import tensorflow as tf
from tensorflow import keras


# def autoencoder_mvtec(channels):
def build_mvtec(channels=3):
    """Model mentionned in the MVTec Paper, originally proposed by Bergmann et Al. 
    Implemented here with an additional convolutional layer at the beginning to 
    accomodate the larger input size of 256 x 256 instead of 128 x 128.    
    Note: Using using Keras's sequential API """
    conv_encoder = keras.models.Sequential(
        [
            # keras.layers.InputLayer(input_shape=(256, 256, channels)),
            keras.layers.Conv2D(
                32,
                kernel_size=4,
                strides=2,
                padding="SAME",
                activation=keras.layers.LeakyReLU(0.2),
                input_shape=(256, 256, channels),
            ),
            # keras.layers.BatchNormalization(),
            keras.layers.Conv2D(
                32,
                kernel_size=4,
                strides=2,
                padding="SAME",
                activation=keras.layers.LeakyReLU(0.2),
            ),
            # keras.layers.BatchNormalization(),
            keras.layers.Conv2D(
                32,
                kernel_size=4,
                strides=2,
                padding="SAME",
                activation=keras.layers.LeakyReLU(0.2),
            ),
            # keras.layers.BatchNormalization(),
            keras.layers.Conv2D(
                32,
                kernel_size=3,
                strides=1,
                padding="SAME",
                activation=keras.layers.LeakyReLU(0.2),
            ),
            # keras.layers.BatchNormalization(),
            keras.layers.Conv2D(
                64,
                kernel_size=4,
                strides=2,
                padding="SAME",
                activation=keras.layers.LeakyReLU(0.2),
            ),
            # keras.layers.BatchNormalization(),
            keras.layers.Conv2D(
                64,
                kernel_size=3,
                strides=1,
                padding="SAME",
                activation=keras.layers.LeakyReLU(0.2),
            ),
            # keras.layers.BatchNormalization(),
            keras.layers.Conv2D(
                128,
                kernel_size=4,
                strides=2,
                padding="SAME",
                activation=keras.layers.LeakyReLU(0.2),
            ),  # CONV6
            # keras.layers.BatchNormalization(),
            keras.layers.Conv2D(
                64,
                kernel_size=3,
                strides=1,
                padding="SAME",
                activation=keras.layers.LeakyReLU(0.2),
            ),
            # keras.layers.BatchNormalization(),
            keras.layers.Conv2D(
                32,
                kernel_size=3,
                strides=1,
                padding="SAME",
                activation=keras.layers.LeakyReLU(0.2),
            ),
            # keras.layers.BatchNormalization(),
            keras.layers.Conv2D(
                100, kernel_size=8, strides=1, padding="VALID", activation="relu"
            ),
            # keras.layers.BatchNormalization(),
            # keras.layers.Flatten(),
        ]
    )

    conv_decoder = keras.models.Sequential(
        [
            # keras.layers.InputLayer(input_shape=(1, 1, 100)),
            keras.layers.Conv2DTranspose(
                32,
                kernel_size=3,
                strides=8,
                padding="VALID",
                # activation="relu",
                activation=keras.layers.LeakyReLU(0.2),
                input_shape=(1, 1, 100),
            ),
            # keras.layers.BatchNormalization(),
            keras.layers.Conv2DTranspose(
                64,
                kernel_size=3,
                strides=1,
                padding="SAME",
                activation=keras.layers.LeakyReLU(0.2),
            ),
            # keras.layers.BatchNormalization(),
            keras.layers.Conv2DTranspose(
                128,
                kernel_size=4,
                strides=1,
                padding="SAME",
                activation=keras.layers.LeakyReLU(0.2),
            ),
            # keras.layers.BatchNormalization(),
            keras.layers.Conv2DTranspose(
                64,
                kernel_size=3,
                strides=2,
                padding="SAME",
                activation=keras.layers.LeakyReLU(0.2),
            ),
            # keras.layers.BatchNormalization(),
            keras.layers.Conv2DTranspose(
                64,
                kernel_size=4,
                strides=1,
                padding="SAME",
                activation=keras.layers.LeakyReLU(0.2),
            ),
            # keras.layers.BatchNormalization(),
            keras.layers.Conv2DTranspose(
                32,
                kernel_size=3,
                strides=2,
                padding="SAME",
                activation=keras.layers.LeakyReLU(0.2),
            ),
            # keras.layers.BatchNormalization(),
            keras.layers.Conv2DTranspose(
                32,
                kernel_size=4,
                strides=1,
                padding="SAME",
                activation=keras.layers.LeakyReLU(0.2),
            ),
            # keras.layers.BatchNormalization(),
            keras.layers.Conv2DTranspose(
                32,
                kernel_size=4,
                strides=2,
                padding="SAME",
                activation=keras.layers.LeakyReLU(0.2),
            ),
            # keras.layers.BatchNormalization(),
            keras.layers.Conv2DTranspose(
                32,
                kernel_size=4,
                strides=2,
                padding="SAME",
                activation=keras.layers.LeakyReLU(0.2),
            ),
            # keras.layers.BatchNormalization(),
            keras.layers.Conv2DTranspose(
                channels,
                kernel_size=4,
                strides=2,
                padding="SAME",
                # activation=keras.layers.LeakyReLU(0.2),
                activation="sigmoid",  # sigmoid
            ),
        ]
    )
    model = keras.models.Sequential([conv_encoder, conv_decoder])
    print(conv_encoder.summary())
    print(conv_decoder.summary())
    print(model.summary())

    return model


def build_mvtec_2(channels=3):
    """Another implementation of mvtec architecture inspired by:
    https://github.com/cheapthrillandwine/Improving_Unsupervised_Defect_Segmentation/blob/master/Improving_AutoEncoder_Samples.ipynb"""
    input_img = keras.layers.Input(shape=(256, 256, channels))
    # Encode-----------------------------------------------------------
    x = keras.layers.Conv2D(32, (4, 4), strides=2, activation="relu", padding="same")(
        input_img
    )
    x = keras.layers.Conv2D(32, (4, 4), strides=2, activation="relu", padding="same")(x)
    x = keras.layers.Conv2D(32, (4, 4), strides=2, activation="relu", padding="same")(x)
    x = keras.layers.Conv2D(32, (3, 3), strides=1, activation="relu", padding="same")(x)
    x = keras.layers.Conv2D(64, (4, 4), strides=2, activation="relu", padding="same")(x)
    x = keras.layers.Conv2D(64, (3, 3), strides=1, activation="relu", padding="same")(x)
    x = keras.layers.Conv2D(128, (4, 4), strides=2, activation="relu", padding="same")(
        x
    )
    x = keras.layers.Conv2D(64, (3, 3), strides=1, activation="relu", padding="same")(x)
    x = keras.layers.Conv2D(32, (3, 3), strides=1, activation="relu", padding="same")(x)
    encoded = keras.layers.Conv2D(1, (8, 8), strides=1, padding="same")(x)

    # Decode---------------------------------------------------------------------
    x = keras.layers.Conv2D(32, (3, 3), strides=1, activation="relu", padding="same")(
        encoded
    )
    x = keras.layers.Conv2D(64, (3, 3), strides=1, activation="relu", padding="same")(x)
    x = keras.layers.UpSampling2D((2, 2))(x)
    x = keras.layers.Conv2D(128, (4, 4), strides=2, activation="relu", padding="same")(
        x
    )
    x = keras.layers.UpSampling2D((2, 2))(x)
    x = keras.layers.Conv2D(64, (3, 3), strides=1, activation="relu", padding="same")(x)
    x = keras.layers.UpSampling2D((2, 2))(x)
    x = keras.layers.Conv2D(64, (4, 4), strides=2, activation="relu", padding="same")(x)
    x = keras.layers.UpSampling2D((2, 2))(x)
    x = keras.layers.Conv2D(32, (3, 3), strides=1, activation="relu", padding="same")(x)
    x = keras.layers.UpSampling2D((2, 2))(x)
    x = keras.layers.Conv2D(32, (4, 4), strides=2, activation="relu", padding="same")(x)
    x = keras.layers.UpSampling2D((4, 4))(x)
    x = keras.layers.Conv2D(32, (4, 4), strides=2, activation="relu", padding="same")(x)
    x = keras.layers.UpSampling2D((2, 2))(x)
    x = keras.layers.Conv2D(32, (8, 8), activation="relu", padding="same")(x)

    x = keras.layers.UpSampling2D((2, 2))(x)
    decoded = keras.layers.Conv2D(
        channels, (8, 8), activation="sigmoid", padding="same"
    )(x)

    model = keras.models.Model(input_img, decoded)
    # keras.utils.plot_model(model, to_file="model.png")
    print(model.summary())

    return model


def build_resnet():
    """The Model is composed of a pretrained encoder (InceptionResNetV2) and a decoder.
    The decoder is inspired by this paper: https://openreview.net/forum?id=B1gikpEtwH
    Note: Using using Keras's functional API """
    # encoder
    base_encoder = keras.applications.inception_resnet_v2.InceptionResNetV2(
        include_top=False,
        weights="imagenet",
        input_tensor=None,
        input_shape=(299, 299, 3),
        pooling=None,
    )
    # # freeze layers
    # for layer in base_encoder.layers:
    #     layer.trainable = False

    encoder = keras.models.Sequential(
        [
            base_encoder,
            keras.layers.Conv2D(
                512, kernel_size=1, strides=1, padding="SAME", activation=None,
            ),
            keras.layers.Conv2D(
                512, kernel_size=1, strides=1, padding="SAME", activation=None,
            ),
        ]
    )
    print(encoder.summary())

    # decoder
    inputs = keras.layers.Input(shape=tuple(encoder.output.shape[-3:]))

    layer_1 = keras.layers.Conv2DTranspose(
        512, kernel_size=4, strides=2, padding="VALID", activation=None,
    )(inputs)
    layer_2 = keras.layers.BatchNormalization()(layer_1)
    layer_3 = keras.layers.ReLU()(layer_2)
    layer_4 = keras.layers.Conv2DTranspose(
        512, kernel_size=3, strides=1, padding="SAME", activation=None,
    )(layer_3)
    layer_5 = keras.layers.BatchNormalization()(layer_4)
    layer_6 = keras.layers.ReLU()(layer_5)
    ####
    add_1 = keras.layers.Add()([layer_1, layer_6])
    ####
    layer_7 = keras.layers.Conv2DTranspose(
        256, kernel_size=3, strides=2, padding="VALID", activation=None,
    )(add_1)
    layer_8 = keras.layers.BatchNormalization()(layer_7)
    layer_9 = keras.layers.ReLU()(layer_8)
    layer_10 = keras.layers.Conv2DTranspose(
        256, kernel_size=3, strides=1, padding="SAME", activation=None,
    )(layer_9)
    layer_11 = keras.layers.BatchNormalization()(layer_10)
    layer_12 = keras.layers.ReLU()(layer_11)
    ####
    add_2 = keras.layers.Add()([layer_7, layer_12])
    ####
    layer_13 = keras.layers.Conv2DTranspose(
        128, kernel_size=4, strides=2, padding="SAME", activation=None,
    )(add_2)
    layer_14 = keras.layers.BatchNormalization()(layer_13)
    layer_15 = keras.layers.ReLU()(layer_14)
    layer_16 = keras.layers.Conv2DTranspose(
        128, kernel_size=3, strides=1, padding="SAME", activation=None,
    )(layer_15)
    layer_17 = keras.layers.BatchNormalization()(layer_16)
    layer_18 = keras.layers.ReLU()(layer_17)
    ####
    add_3 = keras.layers.Add()([layer_13, layer_18])
    ####
    layer_19 = keras.layers.Conv2DTranspose(
        64, kernel_size=3, strides=2, padding="VALID", activation=None,
    )(add_3)
    layer_20 = keras.layers.BatchNormalization()(layer_19)
    layer_21 = keras.layers.ReLU()(layer_20)
    layer_22 = keras.layers.Conv2DTranspose(
        64, kernel_size=3, strides=1, padding="SAME", activation=None,
    )(layer_21)
    layer_23 = keras.layers.BatchNormalization()(layer_22)
    layer_24 = keras.layers.ReLU()(layer_23)
    ####
    add_4 = keras.layers.Add()([layer_19, layer_24])
    ####
    layer_25 = keras.layers.Conv2DTranspose(
        3,
        kernel_size=3,
        strides=2,
        padding="VALID",
        activation=keras.activations.sigmoid,
    )(add_4)

    decoder = keras.models.Model(inputs=inputs, outputs=layer_25)
    print(decoder.summary())
    model = keras.models.Sequential([encoder, decoder])
    # keras.utils.plot_model(decoder, to_file="decoder_resnet.png")
    print(model.summary())

    return model, base_encoder


# ==================================================================
# def autoencoder_NASNetMobile(channels):
#     base_encoder = keras.applications.nasnet.NASNetMobile(
#         input_shape=(224, 224, 3),
#         include_top=False,
#         weights="imagenet",
#         input_tensor=None,
#         pooling=None,
#     )
#     print(base_encoder.summary())

#     # decoder
#     inputs = keras.layers.Input(shape=tuple(base_encoder.output.shape[-3:]))

#     layer_1 = keras.layers.Conv2DTranspose(
#         512, kernel_size=4, strides=2, padding="SAME", activation=None,
#     )(inputs)
#     layer_2 = keras.layers.BatchNormalization()(layer_1)
#     layer_3 = keras.layers.ReLU()(layer_2)


# ==================================================================
# ==================================================================

# def autoencoder_inception_resnet_v2_old(channels):

#     # encoder
#     base_encoder = keras.applications.inception_resnet_v2.InceptionResNetV2(
#         include_top=False,
#         weights="imagenet",
#         input_tensor=None,
#         input_shape=(299, 299, 3),
#         pooling=None,
#     )
#     # print(base_encoder.summary())

#     conv_encoder = keras.models.Sequential(
#         [
#             base_encoder,
#             keras.layers.Conv2D(
#                 512, kernel_size=1, strides=1, padding="SAME", activation=None,
#             ),
#             keras.layers.Conv2D(
#                 512, kernel_size=1, strides=1, padding="SAME", activation=None,
#             ),
#         ]
#     )
#     print(conv_encoder.summary())

#     # decoder
#     inputs = keras.layers.Input(shape=tuple(conv_encoder.output.shape[-3:]))

#     layer_1 = keras.layers.Conv2DTranspose(
#         512, kernel_size=4, strides=2, padding="SAME", activation=None,
#     )(inputs)
#     layer_2 = keras.layers.BatchNormalization()(layer_1)
#     layer_3 = keras.layers.ReLU()(layer_2)
#     layer_4 = keras.layers.Conv2DTranspose(
#         512, kernel_size=3, strides=1, padding="SAME", activation=None,
#     )(layer_3)
#     layer_5 = keras.layers.BatchNormalization()(layer_4)
#     layer_6 = keras.layers.ReLU()(layer_5)
#     ####
#     add_1 = keras.layers.Add()([layer_1, layer_6])
#     ####
#     layer_7 = keras.layers.Conv2DTranspose(
#         256, kernel_size=4, strides=2, padding="SAME", activation=None,
#     )(add_1)
#     layer_8 = keras.layers.BatchNormalization()(layer_7)
#     layer_9 = keras.layers.ReLU()(layer_8)
#     layer_10 = keras.layers.Conv2DTranspose(
#         256, kernel_size=3, strides=1, padding="SAME", activation=None,
#     )(layer_9)
#     layer_11 = keras.layers.BatchNormalization()(layer_10)
#     layer_12 = keras.layers.ReLU()(layer_11)
#     ####
#     add_2 = keras.layers.Add()([layer_7, layer_12])
#     ####
#     layer_13 = keras.layers.Conv2DTranspose(
#         128, kernel_size=4, strides=2, padding="SAME", activation=None,
#     )(add_2)
#     layer_14 = keras.layers.BatchNormalization()(layer_13)
#     layer_15 = keras.layers.ReLU()(layer_14)
#     layer_16 = keras.layers.Conv2DTranspose(
#         128, kernel_size=3, strides=1, padding="SAME", activation=None,
#     )(layer_15)
#     layer_17 = keras.layers.BatchNormalization()(layer_16)
#     layer_18 = keras.layers.ReLU()(layer_17)
#     ####
#     add_3 = keras.layers.Add()([layer_13, layer_18])
#     ####
#     layer_19 = keras.layers.Conv2DTranspose(
#         64, kernel_size=4, strides=2, padding="SAME", activation=None,
#     )(add_3)
#     layer_20 = keras.layers.BatchNormalization()(layer_19)
#     layer_21 = keras.layers.ReLU()(layer_20)
#     layer_22 = keras.layers.Conv2DTranspose(
#         64, kernel_size=3, strides=1, padding="SAME", activation=None,
#     )(layer_21)
#     layer_23 = keras.layers.BatchNormalization()(layer_22)
#     layer_24 = keras.layers.ReLU()(layer_23)
#     ####
#     add_4 = keras.layers.Add()([layer_19, layer_24])
#     ####
#     layer_25 = keras.layers.Conv2DTranspose(
#         3,
#         kernel_size=4,
#         strides=2,
#         padding="SAME",
#         activation=keras.activations.sigmoid,
#     )(add_4)

#     conv_decoder = keras.models.Model(inputs=inputs, outputs=layer_25)

#     model = keras.models.Sequential([conv_encoder, conv_decoder])

#     return model

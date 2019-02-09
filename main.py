import tensorflow as tf

# const1 = tf.constant(4.0, name="const1")
# graph1 = tf.get_default_graph()
# assert const1.graph is graph1
#
# const2 = tf.constant(30, name="const2")
# assert const2.graph is graph1
#
# graph2 = tf.Graph()
#
# with graph2.as_default():
#     const3 = tf.constant(20)
#     assert const3.graph is graph2
#
# graph3 = tf.Graph()
# with graph3.as_default():
#     matrix1 = tf.constant([[3., 3.], [3., 3.]], name="matrix1")
#     matrix2 = tf.constant([[2., 2.], [2., 2.]], name="matrix2")
#
#     product_graph = tf.matmul(matrix1, matrix2, name="product")
#
# with tf.Session(graph=graph3) as sess:
#     result = sess.run([product_graph])
#     print(result)


grafo1 = tf.Graph()
with grafo1.as_default():
    # Variable que guardará el sumatorio en las distintas ejecuciones
    sumatorio = tf.Variable(0, name="counter")
    # Variable de entrada (feed) = contador
    input1 = tf.placeholder(tf.int32)

    # Logica de cada paso
    valor_operacion = tf.multiply(input1, input1)
    flujo = tf.assign_add(sumatorio, valor_operacion)

with tf.Session(graph=grafo1) as sess:
    # Las variables deben inicializarse explicitamente
    tf.initialize_all_variables().run()

    for contador in range(3):
        estado = sess.run([flujo, valor_operacion], feed_dict={input1: contador})
        print("Iteracion {}: {}".format(contador, estado))

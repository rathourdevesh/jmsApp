import sys
sys.path.append("/home/devesh/MQClient/javax.jms-api-2.0.1.jar")
sys.path.append("/home/devesh/MQClient/com.ibm.mq.allclient-9.1.4.0.jar")


from javax.jms import Destination;
from javax.jms import JMSConsumer;
from javax.jms import JMSContext;
from javax.jms import JMSException;
from javax.jms import JMSProducer;
from javax.jms import TextMessage;

from com.ibm.msg.client.jms import JmsConnectionFactory;
from com.ibm.msg.client.jms import JmsFactoryFactory;
from com.ibm.msg.client.wmq import WMQConstants;

ff = JmsFactoryFactory.getInstance(WMQConstants.WMQ_PROVIDER);
cf = ff.createConnectionFactory();

cf.setStringProperty(WMQConstants.WMQ_HOST_NAME, "localhost");
cf.setIntProperty(WMQConstants.WMQ_PORT, 1414);
cf.setStringProperty(WMQConstants.WMQ_CHANNEL, "DEV.APP.SVRCONN");
cf.setIntProperty(WMQConstants.WMQ_CONNECTION_MODE, WMQConstants.WMQ_CM_CLIENT);
cf.setStringProperty(WMQConstants.WMQ_QUEUE_MANAGER, "QM1");
cf.setStringProperty(WMQConstants.WMQ_APPLICATIONNAME, "JmsPutGet (JMS)");
cf.setBooleanProperty(WMQConstants.USER_AUTHENTICATION_MQCSP, True);
cf.setStringProperty(WMQConstants.USERID, "app");
cf.setStringProperty(WMQConstants.PASSWORD, "78960");

context = cf.createContext();

destination = context.createQueue("queue:///" + "DEV.QUEUE.1");
message = "Test msg from Jython";
producer = context.createProducer();
producer.send(destination, message);
print("Sent message: " , message);


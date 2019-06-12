from maltego import MaltegoMsg, MaltegoTransform
import socket

def get_exception_message(msg="An exception occurred with the transform. Check the logs for more details."):
   return """<MaltegoMessage>
   <MaltegoTransformResponseMessage>
      <Entities>
      </Entities>
      <UIMessages>
         <UIMessage MessageType='PartialError'>
               %s
         </UIMessage>
      </UIMessages>
   </MaltegoTransformResponseMessage>
   </MaltegoMessage>""" % msg


def DNStoIPTransform(request,response):
   dns_name = request.Value

   try:
      ip_address = socket.gethostbyname(dns_name)
      response.addEntity("maltego.IPv4Address", ip_address)
   except socket.error as e:
      response.addUIMessage("Error: " + str(e), UIM_TYPES["partial"])

   # Write the slider value as a UI message - just for fun
   response.addUIMessage("Slider value is at: " + str(request.Slider))

def sampleTransform(request,response):
   #This is just an example transform
   entityValue = request.Value
   response.addEntity("maltego.Phrase", "Hi %s" % entityValue)

def handler(event,context):
   response = MaltegoTransform() # Maltego XML Response Object
   if("body" in event):
      request = MaltegoMsg(event["body"]) # Maltego XML Request Object (what we got in)
      sampleTransform(request,response)
      xmlResponse = response.returnOutput()
   else:
      xmlResponse = get_exception_message() # We didnt get a body? yikes!

   return {
      'body': '{}'.format(xmlResponse),
      'headers': {
      'Content-Type': 'text/xml'
      },
      'statusCode': 200
   }

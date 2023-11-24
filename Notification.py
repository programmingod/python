from plyer import notification  
  
notification_title = "Hello Hello Hello"
notification_message = "How much wood could a woodchuck chuck if a woodchuck could chuck wood?"

notification.notify(  
    title = notification_title,  
    message = notification_message,  
    app_icon = None,  
    timeout = 10,  
    toast = False  
    )  
# Docker commands
Build

    $ docker build --rm=true -t rabbitmqdemo:latest .
    
Run
    
    $ docker run -p 127.0.0.1:5000:5000 -t rabbitmqdemo:latest
    
Kill
    
    $ docker ps | awk 'NR==2{print $1}' | xargs docker kill
    
    

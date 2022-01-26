use std::net::{TcpListener, TcpStream};
use std::io::{Result, Read, Write};

/// This struct is main server which serve actual internet traffics.
pub struct Server {
    listener: TcpListener,
}

impl Server {

    pub async fn new(port: &str) -> Result<Self> {

        let url = format!("127.0.0.1:{}", port);
        let listener = TcpListener::bind(&url)?;

        println!("Server is running on: {}", &url);

        Ok(Server {
            listener,
        })
    }

    pub async fn run_server(&self) -> Result<()> {

        loop {
            let mut result = self.listener.accept().unwrap();
            let mut stream = result.0;
            let addr = result.1;

            //let _ = stream.readable().await;

            let mut buf = String::new();

            match stream.read_to_string(&mut buf) {
                Ok(_) => {

                    println!("Address {}: ", addr);
                    println!("Request: {}", &buf);

                    self.handle(stream);

                },
                Err(e) => {
                    return Err(e.into());
                }
            }
        }
    }

    /// This is actual method that works as SERVER.
    fn handle(&self, mut stream: TcpStream) {

        let response = "HTTP/1.1 200 OK\r\n\r\n";

        stream.write(response.as_bytes()).unwrap();
        stream.flush().unwrap();
    }
}

use tokio::{net::{TcpStream, TcpListener}, io::AsyncReadExt};
use std::error::Error;
use std::io::{Result};

pub struct Server {
    listener: TcpListener,
}

impl Server {

    pub async fn new(port: &str) -> Result<Self> {

        let url = format!("127.0.0.1:{port}");
        let listener = TcpListener::bind(url).await?;

        Ok(Server {
            listener,
        })
    }

    pub async fn run_server(&self) -> Result<()> {

        loop {
            let (socket, _) = self.listener.accept().await.unwrap();
            self.handle_connection(socket).await;
        }
    }

    async fn handle_connection(&self, mut stream: TcpStream) -> Result<(), Box<dyn Error>> {

        stream.readable().await;

        let mut buf = [0; 4096];

        match stream.try_read(&mut buf) {
            Ok(0) => break,
            Ok(n) => {
                println!("Request: {}", String::from_utf8_lossy(&buf[..]));
            },
            Err(ref e) if e.kind() == io::ErrorKind::WouldBlock => {
                continue;
            },
            Err(e) => {
                return Err(e.into());
            }
        }
    }
}

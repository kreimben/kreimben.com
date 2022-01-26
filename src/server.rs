use tokio::{net::{TcpStream, TcpListener}, io};
use std::io::{Result};
use std::task::{Context, Poll};

pub struct Server {
    listener: TcpListener,
}

impl Server {

    pub async fn new(port: &str) -> Result<Self> {

        let url = format!("127.0.0.1:{}", port);
        let listener = TcpListener::bind(url).await?;

        Ok(Server {
            listener,
        })
    }

    pub async fn run_server(&self) -> Result<()> {

        loop {
            let (socket, _) = self.listener.accept().await.unwrap();
            //self.handle_connection(socket).await;

            socket.readable().await;

            let mut buf = [0; 4096];

            match socket.try_read(&mut buf) {
                Ok(0) => break,
                Ok(_) => {
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

        Ok(())
    }
}
use tokio::{net::TcpListener, io};
use std::io::Result;

/// This struct is main server which serve actual internet traffics.
pub struct Server {
    listener: TcpListener,
}

impl Server {

    pub async fn new(port: &str) -> Result<Self> {

        let url = format!("127.0.0.1:{}", port);
        let listener = TcpListener::bind(&url).await?;

        println!("Server is running on: {}", &url);

        Ok(Server {
            listener,
        })
    }

    pub async fn run_server(&self) -> Result<()> {

        loop {
            let (socket, addr) = self.listener.accept().await.unwrap();

            let _ = socket.readable().await;

            let mut buf = [0; 512];

            match socket.try_read(&mut buf) {
                Ok(0) => break,
                Ok(_) => {

                    let result = String::from_utf8_lossy(&buf[..]);
                    //let json = serde_json::json!(result);

                    println!("Address {}: ", addr);
                    println!("Request: {}", result);

                    self.handle();
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

    fn handle(&self) {

    }
}

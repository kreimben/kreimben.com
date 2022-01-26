mod server;
mod instagram;

use tokio::runtime::Runtime;

#[tokio::main]
async fn main() {

    let runtime = Runtime::new().unwrap();
    let result = runtime.block_on(async {

        let server = server::Server::new("5000");
        server.run_server().await;
    });

    //let insta = instagram::Instagram::new();
    //insta.get_posts().await;
}

mod server;
mod instagram;

#[tokio::main]
async fn main() {

    let server = server::Server::new();
    server.run_server("5000");

    let insta = instagram::Instagram::new();

    //insta.get_posts().await;
}

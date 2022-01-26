mod server;
mod instagram;

#[tokio::main]
async fn main() {

    let server = server::Server::new("5000").await.unwrap();
    let _result = server.run_server().await;

    //let insta = instagram::Instagram::new();
    //insta.get_posts().await;
}

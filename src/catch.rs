use rocket::Request;

#[catch(404)]
pub fn not_found(req: &Request) -> String {
    format!("Sorry, {} is not a valid path.", req.uri())
}

#[catch(500)]
pub fn internal_error(req: &Request) -> String {
    format!("Whoops! Internal Error!\nPlease notice <a href='mailto:aksidion@kreimben.com'>me.</a>")
}

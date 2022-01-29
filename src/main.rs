mod catch;

#[macro_use] extern crate rocket;

use rocket::response::content::Json;
use rocket::{http::Status};


#[get("/")]
fn center() -> String {
    format!("Hello, World!")
}

#[get("/fail")]
fn just_fail() -> Status {
    Status::NotAcceptable
}

#[get("/json")]
fn json() -> Json<String> {
    let s = format!("{{status: success}}");
    Json(s)
}

#[launch]
fn rocket() -> _ {
    rocket::build().mount("/", routes![
        center,
        json,
        just_fail
    ])
                   .register("/", catchers![
                       catch::not_found,
                       catch::internal_error
                   ])
}

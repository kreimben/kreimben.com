mod catch;

#[macro_use] extern crate rocket;

use rocket::{http::Status};
use rocket::serde::{Serialize};

#[get("/")]
fn center() -> String {
    format!("Hello, World!")
}

#[get("/fail")]
fn just_fail() -> Status {
    panic!("");
    Status::NotAcceptable
}

#[get("/json")]
fn json() -> Json<String> {
    //Json{format!("status: success")}
    serde_json::json!("status: success")
}

#[launch]
fn rocket() -> _ {
    rocket::build().mount("/", routes![
        center,
        just_fail
    ])
                   .register("/", catchers![
                       catch::not_found,
                       catch::internal_error
                   ])
}

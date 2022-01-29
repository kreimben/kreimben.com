mod catch;
mod jsonboilerplate;//::response::{Success, Fail};

#[macro_use] extern crate rocket;

use rocket::response;
use rocket::response::content::Json;
use rocket::{http::Status};

#[get("/fail")]
fn just_fail() -> Status {
    Status::NotAcceptable
}

#[get("/")]
fn center() -> Json<jsonboilerplate::response::Success> {
    let s = jsonboilerplate::response::Success {
        success: true,
        content: String::from("Hello, world!")
    };
    Json(s)
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

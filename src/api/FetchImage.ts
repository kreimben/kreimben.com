async function mainImageURL(): string {
  const rawURL =
    "https://api.nasa.gov/planetary/apod?api_key=QW1wu60CBhtBFhNt8snLVgFrdFqu1htLu6jc47v2";
  const data = await fetch(rawURL);
  const json = await data.json();

  return json.url;
}

export default mainImageURL;

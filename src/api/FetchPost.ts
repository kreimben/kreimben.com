const baseURL = "https://strapi.kreimben.com/";

const FetchPost = async (id: string): Promise<any> => {
  let postfix = null;
  if (id !== null || id !== undefined) {
    postfix = "/" + id;
  }

  const op = {
    method: "GET",
  };

  const completeURL = baseURL + "posts" + postfix;
  //alert(completeURL);
  const response = await fetch(completeURL, op);
  const json = await response.json();
  return json;
};

export { FetchPost };

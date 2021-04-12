const baseURL = "https://strapi.kreimben.com/";

const FetchCategory = async (id: string): Promise<any> => {
  let postfix = null;
  if (id !== null || id !== undefined) {
    postfix = "/" + id;
  }

  const op = {
    method: "GET",
  };

  const completeURL = baseURL + "categories" + postfix;
  //alert(completeURL);
  const response = await fetch(completeURL, op);
  const json = response.json();
  return json;
};

export { FetchCategory };

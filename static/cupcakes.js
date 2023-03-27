class Cupcake {
  constructor(flavor, size, rating, image) {
    this.flavor = flavor;
    this.size = size;
    this.rating = rating;
    this.image = image;
  }

  async create() {
    try {
      const response = await axios.post("/api/cupcakes", {
        flavor: this.flavor,
        size: this.size,
        rating: this.rating,
        image: this.image,
      });
      console.log(response.data);
      alert("Cupcake was created!");

      const cupcake = new Cupcake(
        cupcake.flavor,
        cupcake.size,
        cupcake.rating,
        cupcake.image
      );
      listCakes([cupcake]);
    } catch (error) {
      console.log(error);
    }
  }
}

const $cakeList = $("#cupcake-list");

function listCakes(cupcakes) {
  $.each(cupcakes, function (i, cupcake) {
    const $img = $("<img>").attr("src", cupcake.image).addClass("card-img-top");
    const $title = $("<h5>").addClass("card-title").text(cupcake.flavor);

    const $content = $("<p>")
      .addClass("card-text")
      .text(`Rating: ${cupcake.rating}`);
    const $divBody = $("<div>")
      .addClass("card-body")
      .append($title)
      .append($content);

    const $card = $("<div>").addClass("card").append($img).append($divBody);
    $cakeList.append($card);
  });
}

async function getCakes() {
  const response = await axios.get("/api/cupcakes");
  const cupcakes = response.data.cupcakes.map(function (cupcake) {
    return new Cupcake(
      cupcake.flavor,
      cupcake.size,
      cupcake.rating,
      cupcake.image
    );
  });
  listCakes(cupcakes);
}
getCakes();

$("#form").on("submit", async function (e) {
  e.preventDefault();
  const flav = $("#cupcakeFlavor").val();
  const sz = $("#cupcakeSize").val();
  const rtg = $("#cupcakeRating").val();
  const img = $("#cupcakeImage").val();

  const cupcake = new Cupcake(flav, sz, rtg, img);
  await cupcake.create();
  await getCakes();
});

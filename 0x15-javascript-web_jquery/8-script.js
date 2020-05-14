$(() => {
  $.get('https://swapi-api.hbtn.io/api/films/?format=json', (data, textStatus) =>	{
  // console.log(data.results, textStatus);
    if (textStatus === 'success') {
      const titles = data.results;
      console.log(titles);
      for (const titleName in titles) {
        // console.log(titles[titleName].title);
        $('#list_movies').append(`<li>${titles[titleName].title}</li>`);
      }
    }
  });
});


  let searchForm = document.querySelector('#searchForm')
  let pageBtn = document.getElementsByClassName('page-link')

  if(searchForm){
    for(let i =0; pageBtn.length > i; i++)
    pageBtn[i].addEventListener('click',function(e){
      e.preventDefault();

      let page = this.dataset.page
      searchForm.innerHTML += `<input value=${page} name="page" hidden/>`

      searchForm.submit()
    })
  }

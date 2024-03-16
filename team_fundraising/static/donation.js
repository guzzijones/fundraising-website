function showhide(ids) {
  for (let i = 0; i < ids.length; i++) {
    var e = document.getElementById(ids[i]);
    e.style.display = (e.style.display == 'block') ? 'none' : 'block';
  }
}

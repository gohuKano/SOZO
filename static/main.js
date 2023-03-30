const listItems = document.querySelectorAll('.header__list__ul li');

listItems.forEach(item => {
  const anchorText = item.querySelector('a').textContent;

  item.addEventListener('mouseover', function() {
    item.querySelector('a').textContent = getHoverText(anchorText);
  });

  item.addEventListener('mouseout', function() {
    item.querySelector('a').textContent = anchorText;
  });
});

function getHoverText(anchorText) {
  switch(anchorText) {
    case 'Ωκεανός':
      return 'Océan';

    case 'Ζώο':
      return 'Animaux';

    case 'Δάσος':
      return 'Forêt';

    case 'Βουνό':
      return 'Montagne';
    default:
      return anchorText;
  }
}

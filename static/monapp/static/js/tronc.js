HTML SCSS JSResult
EDIT ON
/*
 * Since the pseudo class :truncated is sadly not a thing, if your truncated box is responsive or the text in the box is of arbitrary size, the following code adds or removes a "truncated" class to simulate the feature.
 *
 * Warning: Doesn't work in all browsers due to the use of ResizeObserver, use something like the window's resize event if you need it to be moar cross browser.
 */
const ps = document.querySelectorAll('p');
const observer = new ResizeObserver(entries => {
  for (let entry of entries) {
    entry.target.classList[entry.target.scrollHeight > entry.contentRect.height ? 'add' : 'remove']('truncated');
  }
});

ps.forEach(p => {
  observer.observe(p);
});
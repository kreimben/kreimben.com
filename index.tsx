import { render } from 'solid-js/web';
import { createSignal } from 'solid-js';

function counter() {
  const [count, setCount] = createSignal(0);

  return <input onclick=(() => { setCount(count() + 1) }) > { count() } < /input>;
}

render(
  () => {
    <counter />
  },
  document.getElementById('app')
);

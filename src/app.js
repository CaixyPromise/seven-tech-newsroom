(() => {
  'use strict';
  const read = id => { const el = document.getElementById(id); return el ? JSON.parse(el.textContent) : null; };
  const pretty = value => new Intl.NumberFormat('en-US', {maximumFractionDigits: 6}).format(value);
  const setBar = (row, value, max, label) => {
    row.querySelector('.bar-fill').style.width = `${max > 0 ? value / max * 100 : 0}%`;
    row.querySelector('.bar-value').textContent = label;
  };
  document.querySelectorAll('[data-filter]').forEach(btn => btn.addEventListener('click', () => {
    const cat = btn.dataset.filter;
    let count = 0;
    document.querySelectorAll('[data-filter]').forEach(b => b.setAttribute('aria-pressed', String(b === btn)));
    document.querySelectorAll('#edition-news [data-category]').forEach(row => {
      row.hidden = cat !== '全部' && row.dataset.category !== cat;
      if (!row.hidden) count++;
    });
    const live = document.getElementById('filter-count');
    if (live) live.textContent = `${cat} · ${count} 条`;
  }));
  const dateSelect = document.getElementById('edition-select');
  if (dateSelect) dateSelect.addEventListener('change', () => { window.location.href = dateSelect.value; });
  const previous = document.getElementById('load-previous');
  if (previous) previous.addEventListener('click', () => {
    const section = document.getElementById('previous-issue');
    const open = previous.getAttribute('aria-expanded') !== 'true';
    previous.setAttribute('aria-expanded', String(open));
    section.hidden = !open;
    previous.firstChild.textContent = (open ? '收起 ' : '继续阅读 ') + previous.dataset.editionLabel + ' ';
    document.getElementById('continuation-status').textContent = open ? `已展开上一期 ${previous.dataset.editionCount} 条新闻。` : '';
  });
  const prices = read('price-data');
  if (prices) {
    const fields = {fixed_text_cost: 'USD / 10K 输入 + 2K 输出', input_per_million: 'USD / 百万输入 Token', output_per_million: 'USD / 百万输出 Token'};
    document.querySelectorAll('[data-price-field]').forEach(btn => btn.addEventListener('click', () => {
      const key = btn.dataset.priceField;
      document.querySelectorAll('[data-price-field]').forEach(b => b.setAttribute('aria-pressed', String(b === btn)));
      const max = Math.max(...prices.map(p => p[key]));
      document.querySelectorAll('#price-chart .bar-row').forEach(row => {
        const p = prices.find(x => x.id === row.dataset.model);
        setBar(row, p[key], max, '$' + pretty(p[key]));
      });
      document.getElementById('price-unit').textContent = fields[key];
    }));
    const input = document.getElementById('input-tokens'), output = document.getElementById('output-tokens');
    if (input && output) {
      const update = () => {
        const ins = Number(input.value), outs = Number(output.value);
        const valid = input.value !== '' && output.value !== '' && Number.isFinite(ins) && Number.isFinite(outs) && ins >= 0 && outs >= 0 && ins <= 1e8 && outs <= 1e8 && Number.isInteger(ins) && Number.isInteger(outs);
        document.getElementById('calc-note').textContent = valid ? '仅估算基本文本 Token 费用；推理 Token、工具、缓存、请求费与上下文价档等可能另计。' : '请输入 0 到 100,000,000 之间的整数 Token 数。';
        document.querySelectorAll('[data-calc-model]').forEach(el => {
          const p = prices.find(x => x.id === el.dataset.calcModel);
          const cost = valid ? ins * p.input_per_million / 1e6 + outs * p.output_per_million / 1e6 : null;
          el.textContent = cost === null ? '—' : cost === 0 ? '$0' : '$' + cost.toLocaleString('en-US', {maximumFractionDigits: 6});
        });
      };
      input.addEventListener('input', update); output.addEventListener('input', update); update();
    }
  }
  const hf = read('hf-data');
  if (hf) document.querySelectorAll('[data-hf-task]').forEach(btn => btn.addEventListener('click', () => {
    document.querySelectorAll('[data-hf-task]').forEach(b => b.setAttribute('aria-pressed', String(b === btn)));
    document.querySelectorAll('[data-hf-group]').forEach(el => el.hidden = el.dataset.hfGroup !== btn.dataset.hfTask);
  }));
  const copy = document.getElementById('copy-feed');
  if (copy) copy.addEventListener('click', async () => {
    const address = document.getElementById('feed-address');
    const status = document.getElementById('copy-status');
    status.textContent = '正在复制…';
    try {
      await Promise.race([navigator.clipboard.writeText(address.value), new Promise((_, reject) => setTimeout(() => reject(new Error('clipboard-timeout')), 1500))]);
      status.textContent = '已复制 RSS 地址。';
    }
    catch { address.focus(); address.select(); status.textContent = '请复制已选中的 RSS 地址。'; }
  });
  const search = document.getElementById('search-query');
  if (search) {
    const items = [...document.querySelectorAll('#search-results [data-search]')];
    const apply = () => {
      const tokens = search.value.trim().toLocaleLowerCase().split(/\s+/).filter(Boolean);
      let count = 0;
      items.forEach(row => { row.hidden = !tokens.every(t => row.dataset.search.includes(t)); if (!row.hidden) count++; });
      document.getElementById('search-count').textContent = tokens.length ? `找到 ${count} 条新闻` : `共 ${count} 条新闻`;
      document.getElementById('search-empty').hidden = count > 0;
    };
    search.value = new URLSearchParams(window.location.search).get('q') || '';
    search.addEventListener('input', apply);
    document.getElementById('search-form').addEventListener('submit', e => { e.preventDefault(); apply(); });
    apply();
  }
})();

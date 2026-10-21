// == Kobo Writing Life 1-Click AutoFiller ==
// Usage: Open Chrome DevTools Console (Cmd+Option+J) on writinglife.kobo.com, paste this and press Enter!
(function() {
    const b = {"title": "NVL72級ラック向け液冷負荷装置を設計し、作る", "subtitle": "要求シートと試作の合格判定", "series": "Data Center Field Guides", "series_number": "1", "author": "Tristan", "publisher": "Data Center Field Guides", "imprint": "Data Center Field Guides", "language": "Japanese", "price": "12.99", "epub": "/Users/geese/Downloads/book/books/01-liquid-load-bank/epub/ja/design-and-build-a-liquid-load-bank.ja.epub", "cover": "/Users/geese/Downloads/book/books/01-liquid-load-bank/figures/covers/ja.jpg", "synopsis": "液冷負荷装置は、NVL72級ラックの代わりになる試験器である。冷却器でも図面でもない。この現場手引は、金属を切る前に何を書き、試作を完成と呼ぶ前にどの門を通すかを示す。残るのは、見知らぬ人に渡せる二つの文書である。要求シートと、試作の受入シート。流量、温度、圧力、継手の数値は、その時点で有効な仕様を引用するまで空欄のままである。"};
    console.log('[+] Starting Kobo 1-Click AutoFill for:', b.title);

    function trigger(el) {
        el.dispatchEvent(new Event('input', { bubbles: true }));
        el.dispatchEvent(new Event('change', { bubbles: true }));
        el.dispatchEvent(new Event('blur', { bubbles: true }));
    }

    function setVal(selectors, val) {
        for (let sel of selectors) {
            const el = document.querySelector(sel);
            if (el) {
                el.focus();
                el.value = val;
                trigger(el);
                console.log('  [✓] Set', sel);
                return true;
            }
        }
        return false;
    }

    // 1. Title & Subtitle
    setVal(['input[name*="Title"]', 'input[id*="title"]', '#eBookTitle', '#Title', 'input[placeholder*="Title"]'], b.title);
    setVal(['input[name*="Subtitle"]', 'input[id*="subtitle"]', '#eBookSubtitle', '#Subtitle', 'input[placeholder*="Subtitle"]'], b.subtitle);

    // 2. Series
    setVal(['input[name*="Series"]', 'input[id*="series"]', '#SeriesName', 'input[placeholder*="Series"]'], b.series);
    setVal(['input[name*="SeriesNumber"]', 'input[id*="seriesNumber"]', '#SeriesNumber', 'input[placeholder*="Number"]'], b.series_number);

    // 3. Author / Contributor
    setVal(['input[name*="Contributor"]', 'input[name*="Author"]', 'input[id*="contributor"]', 'input[id*="author"]', 'input[placeholder*="Author"]'], b.author);

    // 4. Publisher & Imprint
    setVal(['input[name*="Publisher"]', 'input[id*="publisher"]', '#PublisherName', 'input[placeholder*="Publisher"]'], b.publisher);
    setVal(['input[name*="Imprint"]', 'input[id*="imprint"]', '#ImprintName', 'input[placeholder*="Imprint"]'], b.imprint);

    // 5. Language
    const langSelect = document.querySelector('select[name*="Language"], select[id*="language"], #Language');
    if (langSelect) {
        for (let opt of langSelect.options) {
            if (opt.text.toLowerCase().includes(b.language.toLowerCase()) || opt.value.toLowerCase().includes(b.language.toLowerCase())) {
                langSelect.value = opt.value;
                trigger(langSelect);
                console.log('  [✓] Set Language to', opt.text);
                break;
            }
        }
    }

    // 6. Synopsis (Textarea or Rich Editor)
    const synTextarea = document.querySelector('textarea[name*="Synopsis"], textarea[id*="synopsis"], textarea[name*="description"], #Synopsis');
    if (synTextarea) {
        synTextarea.value = b.synopsis;
        trigger(synTextarea);
        console.log('  [✓] Set Synopsis textarea');
    }
    const richEditor = document.querySelector('.ck-editor__editable, [contenteditable="true"]');
    if (richEditor) {
        richEditor.innerText = b.synopsis;
        trigger(richEditor);
        console.log('  [✓] Set Synopsis rich editor');
    }

    // 7. Pricing & DRM (If on Pricing step)
    setVal(['input[name*="Price"]', 'input[id*="price"]', '#Price', 'input[placeholder*="0.00"]'], b.price);
    
    // Checkboxes / Radios
    const drmRadio = document.querySelector('input[name*="drm"][value*="true"], input[id*="drm-yes"]');
    if (drmRadio) { drmRadio.click(); trigger(drmRadio); }
    
    const koboPlus = document.querySelector('input[name*="koboPlus"], input[id*="koboPlus"]');
    if (koboPlus && !koboPlus.checked) { koboPlus.click(); trigger(koboPlus); }

    // Notification toast
    const toast = document.createElement('div');
    toast.style.cssText = 'position:fixed;top:20px;right:20px;background:#10b981;color:#fff;padding:12px 20px;border-radius:8px;font-weight:bold;z-index:999999;box-shadow:0 10px 25px rgba(0,0,0,0.4);font-family:sans-serif;';
    toast.innerHTML = '⚡ Kobo AutoFill Complete!<br><span style="font-size:12px;font-weight:normal;">EPUB: ' + b.epub.split('/').pop() + '</span>';
    document.body.appendChild(toast);
    setTimeout(() => toast.remove(), 6000);
})();

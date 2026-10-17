/**
 * Global Instant Search Component for Data Center Field Guides
 * Features:
 * - Cmd+K / Ctrl+K and '/' universal keyboard shortcuts
 * - Instant client-side fuzzy search across all 68+ field protocols
 * - Keyboard navigation (Up / Down / Enter / Esc)
 * - Volume badges and highlighted matching terms
 * - Path-aware URL resolution for root, /blog/, and /book/ directories
 */
(function () {
  'use strict';

  // Determine current directory depth to resolve relative URLs
  const pathname = window.location.pathname;
  const isSubdir = pathname.includes('/blog/') || pathname.includes('/book/');
  const blogPrefix = isSubdir ? '../blog/' : 'blog/';

  // Modal HTML Template
  const modalHTML = `
  <div class="search-modal-backdrop" id="search-modal-backdrop" aria-hidden="true" style="display:none;">
    <div class="search-modal-dialog" role="dialog" aria-modal="true" aria-label="Search Protocols">
      <div class="search-modal-header">
        <svg class="search-modal-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
          <circle cx="11" cy="11" r="8"></circle>
          <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
        </svg>
        <input type="text"
               id="search-modal-input"
               class="search-modal-input"
               placeholder="Search protocols, equations, checklists (e.g. NVL72, CFD, SOP, retainage)..."
               autocomplete="off"
               spellcheck="false" />
        <button type="button" class="search-modal-close" id="search-modal-close" aria-label="Close search (Esc)">&times;</button>
      </div>

      <div class="search-modal-filter-row">
        <span class="filter-row-label">Volume:</span>
        <div class="filter-pill-group">
          <button type="button" class="search-pill active" data-volume="all">All (68)</button>
          <button type="button" class="search-pill" data-volume="1">Vol 01</button>
          <button type="button" class="search-pill" data-volume="2">Vol 02</button>
          <button type="button" class="search-pill" data-volume="3">Vol 03</button>
          <button type="button" class="search-pill" data-volume="4">Vol 04</button>
          <button type="button" class="search-pill" data-volume="5">Vol 05</button>
          <button type="button" class="search-pill" data-volume="6">Vol 06</button>
          <button type="button" class="search-pill" data-volume="7">Vol 07</button>
          <button type="button" class="search-pill" data-volume="8">Vol 08</button>
          <button type="button" class="search-pill" data-volume="9">Vol 09</button>
        </div>
      </div>

      <div class="search-modal-results" id="search-modal-results">
        <div class="search-empty-state">Type a keyword above or select a volume to filter protocols.</div>
      </div>

      <div class="search-modal-footer">
        <div class="search-shortcuts">
          <span><kbd class="key-hint">↑</kbd><kbd class="key-hint">↓</kbd> navigate</span>
          <span><kbd class="key-hint">↵</kbd> select</span>
          <span><kbd class="key-hint">esc</kbd> close</span>
        </div>
        <div class="search-stat" id="search-stat-count">68 protocols indexed</div>
      </div>
    </div>
  </div>
  `;

  // Modal CSS Styles
  const modalCSS = `
  .search-modal-backdrop {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(5, 8, 15, 0.82);
    backdrop-filter: blur(8px);
    -webkit-backdrop-filter: blur(8px);
    z-index: 9999;
    display: flex;
    align-items: flex-start;
    justify-content: center;
    padding: 4.5rem 1rem 2rem;
    animation: fadeInModal 0.18s ease-out;
  }
  @keyframes fadeInModal {
    from { opacity: 0; }
    to { opacity: 1; }
  }
  .search-modal-dialog {
    background: #111726;
    border: 1px solid #1e283d;
    border-radius: 12px;
    width: 100%;
    max-width: 640px;
    box-shadow: 0 25px 60px -15px rgba(0, 0, 0, 0.85), 0 0 0 1px rgba(37, 99, 235, 0.25);
    overflow: hidden;
    display: flex;
    flex-direction: column;
    max-height: 80vh;
  }
  .search-modal-header {
    display: flex;
    align-items: center;
    padding: 1rem 1.25rem;
    border-bottom: 1px solid #1e283d;
    gap: 0.85rem;
    background: #090d16;
  }
  .search-modal-icon {
    color: #3b82f6;
    flex-shrink: 0;
  }
  .search-modal-input {
    flex: 1;
    background: transparent;
    border: none;
    outline: none;
    font-size: 1.05rem;
    color: #f8fafc;
    font-family: inherit;
  }
  .search-modal-input::placeholder {
    color: #64748b;
  }
  .search-modal-close {
    background: transparent;
    border: none;
    color: #94a3b8;
    font-size: 1.5rem;
    line-height: 1;
    cursor: pointer;
    padding: 0.2rem 0.4rem;
    border-radius: 4px;
    transition: color 0.15s;
  }
  .search-modal-close:hover {
    color: #fff;
  }
  .search-modal-filter-row {
    display: flex;
    align-items: center;
    padding: 0.65rem 1.25rem;
    background: #0d121f;
    border-bottom: 1px solid #1e283d;
    gap: 0.6rem;
    overflow-x: auto;
  }
  .filter-row-label {
    font-size: 0.72rem;
    font-weight: 700;
    color: #64748b;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    flex-shrink: 0;
  }
  .filter-pill-group {
    display: flex;
    align-items: center;
    gap: 0.35rem;
    flex-wrap: nowrap;
  }
  .search-pill {
    background: #162035;
    border: 1px solid #232f48;
    color: #94a3b8;
    font-size: 0.72rem;
    font-weight: 600;
    padding: 0.2rem 0.55rem;
    border-radius: 9999px;
    cursor: pointer;
    white-space: nowrap;
    transition: all 0.15s;
  }
  .search-pill:hover {
    color: #fff;
    border-color: #3b82f6;
  }
  .search-pill.active {
    background: rgba(37, 99, 235, 0.15);
    border-color: #2563eb;
    color: #3b82f6;
  }
  .search-modal-results {
    overflow-y: auto;
    padding: 0.5rem;
    max-height: 480px;
  }
  .search-empty-state {
    padding: 3rem 1.5rem;
    text-align: center;
    color: #64748b;
    font-size: 0.95rem;
  }
  .search-result-item {
    display: flex;
    flex-direction: column;
    padding: 0.85rem 1rem;
    border-radius: 8px;
    text-decoration: none;
    color: inherit;
    border: 1px solid transparent;
    transition: all 0.12s ease;
    margin-bottom: 0.25rem;
  }
  .search-result-item:hover,
  .search-result-item.is-selected {
    background: #172033;
    border-color: rgba(37, 99, 235, 0.4);
  }
  .search-result-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 0.5rem;
    margin-bottom: 0.35rem;
  }
  .search-result-badges {
    display: flex;
    align-items: center;
    gap: 0.4rem;
  }
  .result-vol-badge {
    font-size: 0.65rem;
    font-weight: 800;
    color: #3b82f6;
    background: rgba(37, 99, 235, 0.12);
    padding: 0.15rem 0.45rem;
    border-radius: 4px;
    border: 1px solid rgba(37, 99, 235, 0.25);
  }
  .result-deep-badge {
    font-size: 0.65rem;
    font-weight: 800;
    color: #d97706;
    background: rgba(217, 119, 6, 0.12);
    padding: 0.15rem 0.45rem;
    border-radius: 4px;
    border: 1px solid rgba(217, 119, 6, 0.25);
  }
  .result-time {
    font-size: 0.72rem;
    color: #64748b;
  }
  .search-result-title {
    font-size: 0.98rem;
    font-weight: 700;
    color: #f8fafc;
    line-height: 1.35;
    margin-bottom: 0.25rem;
  }
  .search-result-desc {
    font-size: 0.82rem;
    color: #94a3b8;
    line-height: 1.45;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
  }
  .search-result-match-highlight {
    background: rgba(217, 119, 6, 0.3);
    color: #fbbf24;
    padding: 0 0.2rem;
    border-radius: 2px;
  }
  .search-modal-footer {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.65rem 1.25rem;
    border-top: 1px solid #1e283d;
    background: #090d16;
    font-size: 0.75rem;
    color: #64748b;
  }
  .search-shortcuts {
    display: flex;
    gap: 0.85rem;
  }
  .key-hint {
    background: #182235;
    border: 1px solid #283954;
    border-radius: 4px;
    padding: 0.15rem 0.35rem;
    color: #cbd5e1;
    font-family: ui-monospace, monospace;
    font-size: 0.7rem;
    margin: 0 0.15rem;
  }

  /* Nav search button trigger */
  .nav-search-trigger {
    display: inline-flex;
    align-items: center;
    gap: 0.55rem;
    background: #121826;
    border: 1px solid #1e283d;
    color: #94a3b8;
    padding: 0.35rem 0.75rem;
    border-radius: 6px;
    font-size: 0.82rem;
    cursor: pointer;
    transition: all 0.2s ease;
    user-select: none;
    font-family: inherit;
  }
  .nav-search-trigger:hover {
    background: #172033;
    border-color: #2563eb;
    color: #f8fafc;
  }
  .nav-search-trigger kbd {
    background: #182235;
    border: 1px solid #283954;
    border-radius: 4px;
    padding: 0.1rem 0.35rem;
    font-size: 0.68rem;
    font-family: ui-monospace, monospace;
    color: #cbd5e1;
  }
  @media (max-width: 640px) {
    .nav-search-trigger span { display: none; }
    .nav-search-trigger kbd { display: none; }
    .search-modal-dialog { max-height: 90vh; }
  }
  `;

  // Inject Styles and Modal DOM
  function initDOM() {
    const styleEl = document.createElement('style');
    styleEl.textContent = modalCSS;
    document.head.appendChild(styleEl);

    const div = document.createElement('div');
    div.innerHTML = modalHTML;
    document.body.appendChild(div.firstElementChild);
  }

  // Highlight matched substrings
  function highlight(text, query) {
    if (!query) return text;
    const escaped = query.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
    const regex = new RegExp(`(${escaped})`, 'gi');
    return text.replace(regex, '<mark class="search-result-match-highlight">$1</mark>');
  }

  // Setup Event Listeners
  function initEvents() {
    const backdrop = document.getElementById('search-modal-backdrop');
    const input = document.getElementById('search-modal-input');
    const closeBtn = document.getElementById('search-modal-close');
    const resultsContainer = document.getElementById('search-modal-results');
    const statCount = document.getElementById('search-stat-count');
    const pillButtons = document.querySelectorAll('.search-pill');

    let activeVolume = 'all';
    let selectedIndex = 0;
    let currentResults = [];

    function openModal() {
      backdrop.style.display = 'flex';
      backdrop.setAttribute('aria-hidden', 'false');
      input.value = '';
      input.focus();
      renderResults();
      document.body.style.overflow = 'hidden';
    }

    function closeModal() {
      backdrop.style.display = 'none';
      backdrop.setAttribute('aria-hidden', 'true');
      document.body.style.overflow = '';
    }

    // Trigger buttons
    document.addEventListener('click', function (e) {
      if (e.target.closest('#open-search-btn') || e.target.closest('.nav-search-trigger')) {
        e.preventDefault();
        openModal();
      }
      if (e.target === backdrop || e.target.closest('#search-modal-close')) {
        closeModal();
      }
    });

    // Universal Key Shortcuts: Cmd+K / Ctrl+K and '/'
    document.addEventListener('keydown', function (e) {
      if ((e.metaKey || e.ctrlKey) && (e.key === 'k' || e.key === 'K')) {
        e.preventDefault();
        if (backdrop.style.display === 'none') {
          openModal();
        } else {
          closeModal();
        }
        return;
      }
      if (e.key === '/' && document.activeElement.tagName !== 'INPUT' && document.activeElement.tagName !== 'TEXTAREA') {
        e.preventDefault();
        openModal();
        return;
      }
      if (backdrop.style.display !== 'none') {
        if (e.key === 'Escape') {
          e.preventDefault();
          closeModal();
        } else if (e.key === 'ArrowDown') {
          e.preventDefault();
          if (currentResults.length > 0) {
            selectedIndex = (selectedIndex + 1) % currentResults.length;
            updateSelection();
          }
        } else if (e.key === 'ArrowUp') {
          e.preventDefault();
          if (currentResults.length > 0) {
            selectedIndex = (selectedIndex - 1 + currentResults.length) % currentResults.length;
            updateSelection();
          }
        } else if (e.key === 'Enter') {
          e.preventDefault();
          const items = resultsContainer.querySelectorAll('.search-result-item');
          if (items[selectedIndex]) {
            items[selectedIndex].click();
          }
        }
      }
    });

    // Volume Pill Selection
    pillButtons.forEach(btn => {
      btn.addEventListener('click', function () {
        pillButtons.forEach(b => b.classList.remove('active'));
        this.classList.add('active');
        activeVolume = this.getAttribute('data-volume');
        renderResults();
      });
    });

    // Input Search
    input.addEventListener('input', function () {
      selectedIndex = 0;
      renderResults();
    });

    function updateSelection() {
      const items = resultsContainer.querySelectorAll('.search-result-item');
      items.forEach((item, idx) => {
        if (idx === selectedIndex) {
          item.classList.add('is-selected');
          item.scrollIntoView({ block: 'nearest' });
        } else {
          item.classList.remove('is-selected');
        }
      });
    }

    function renderResults() {
      const query = input.value.trim().toLowerCase();
      const indexData = window.FIELD_GUIDE_SEARCH_INDEX || [];

      let filtered = indexData.filter(item => {
        // Volume check
        if (activeVolume !== 'all' && String(item.book_num) !== activeVolume) {
          return false;
        }
        // Query check
        if (!query) return true;
        const inTitle = item.title.toLowerCase().includes(query);
        const inDesc = item.desc.toLowerCase().includes(query);
        const inKw = (item.keywords || '').toLowerCase().includes(query);
        const inVol = (item.book_title || '').toLowerCase().includes(query);
        return inTitle || inDesc || inKw || inVol;
      });

      currentResults = filtered;
      statCount.textContent = `${filtered.length} protocols found`;

      if (filtered.length === 0) {
        resultsContainer.innerHTML = `<div class="search-empty-state">No protocols matching "<strong>${query}</strong>" found. Try searching for NVL72, CFD, SOP, ISA, or retainage.</div>`;
        return;
      }

      // Generate Result Cards
      const itemsHtml = filtered.map((item, idx) => {
        const isSel = idx === selectedIndex ? ' is-selected' : '';
        const deepBadge = item.is_deep_dive ? '<span class="result-deep-badge">★ DEEP-DIVE</span>' : '';
        const href = `${blogPrefix}${item.slug}`;

        return `
        <a href="${href}" class="search-result-item${isSel}" data-idx="${idx}">
          <div class="search-result-header">
            <div class="search-result-badges">
              <span class="result-vol-badge">VOL 0${item.book_num}</span>
              ${deepBadge}
            </div>
            <span class="result-time">⏱️ ${item.read_mins}m</span>
          </div>
          <div class="search-result-title">${highlight(item.title, query)}</div>
          <div class="search-result-desc">${highlight(item.desc, query)}</div>
        </a>
        `;
      }).join('');

      resultsContainer.innerHTML = itemsHtml;
    }
  }

  // Run on DOM ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function () {
      initDOM();
      initEvents();
    });
  } else {
    initDOM();
    initEvents();
  }
})();

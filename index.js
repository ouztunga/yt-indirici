let LOGO_DATA = "";
let currentQuality = "1080";
let currentFormat = "mp4";
let analyzeTimeout = null;
let isDownloading = false;
let currentUrl = "";
let isPlaylistActive = false;
let playlistEntries = [];
let allSizes = {};          // Tüm çözünürlüklerin boyutları (Python'dan gelir)

// ═══════════════════════════════════════════════════════════
//  OTOMATİK ANALİZ
// ═══════════════════════════════════════════════════════════

function autoAnalyze(url) {
    if (isDownloading) return;
    if (analyzeTimeout) clearTimeout(analyzeTimeout);

    if (!url || url.trim() === "") {
        resetUI();
        return;
    }
    if (url.length < 8 || (!url.startsWith('http://') && !url.startsWith('https://'))) return;

    currentUrl = url;
    document.getElementById('statusText').innerText = "Video verileri analiz ediliyor...";
    document.getElementById('progressBar').style.width = '0%';

    const startBtn = document.getElementById('startBtn');
    startBtn.disabled = true;
    startBtn.classList.add('opacity-50', 'cursor-not-allowed');
    startBtn.classList.remove('hover:opacity-90');

    // Önizlemeyi sıfırla
    const thumb = document.getElementById('videoThumb');
    thumb.src = LOGO_DATA || "logo.png";
    thumb.classList.add('max-w-[70%]', 'max-h-[70%]');
    thumb.classList.remove('w-full', 'h-full', 'object-cover');
    document.getElementById('videoTitle').innerText = "Video Bekleniyor...";
    document.getElementById('sizeBadge').classList.add('hidden');

    // Playlist durumunu sıfırla
    isPlaylistActive = false;
    playlistEntries = [];
    allSizes = {};
    enableAllResolutionButtons();
    document.getElementById('playlistScrollContainer').classList.add('hidden');
    document.getElementById('thumbContainer').classList.remove('hidden');
    document.getElementById('detailsBox').classList.remove('hidden');

    analyzeTimeout = setTimeout(() => {
        document.getElementById('inputLoader').classList.remove('hidden');
        if (window.pywebview && window.pywebview.api) {
            pywebview.api.analyze(url, currentQuality);
        }
    }, 1000);
}

// ═══════════════════════════════════════════════════════════
//  ÇÖZÜNÜRLÜK SEÇİMİ
// ═══════════════════════════════════════════════════════════

function setQuality(q, btn) {
    currentQuality = q;

    // Buton görsellerini güncelle
    document.querySelectorAll('.res-btn').forEach(b => {
        b.classList.remove('active');
        b.classList.add('text-gray-400');
    });
    btn.classList.add('active');
    btn.classList.remove('text-gray-400');

    // Playlist modunda listeyi yeniden render et
    if (isPlaylistActive) {
        renderPlaylistItems();
        return;
    }

    // Boyut badge'ini allSizes'dan göster (Python'a çağrı yok — anlık)
    const badge = document.getElementById('sizeBadge');
    if (allSizes && allSizes[q]) {
        badge.innerText = allSizes[q];
        badge.classList.remove('hidden');
    } else {
        badge.classList.add('hidden');
    }
}

// ═══════════════════════════════════════════════════════════
//  UI GÜNCELLEME (Python'dan çağrılır)
// ═══════════════════════════════════════════════════════════

function updateUI(title, imgUrl, sizes, source_url, playlist_entries, max_height) {
    // URL değiştiyse eski analizi gösterme
    const currentInput = document.getElementById('urlInput').value;
    if (!currentInput || currentInput.trim() === "" || currentInput !== source_url) {
        return;
    }

    document.getElementById('inputLoader').classList.add('hidden');

    // İndirme butonunu aktif et ve görünür yap, bitiş/aktif kontrolleri gizle
    const startBtn = document.getElementById('startBtn');
    startBtn.disabled = false;
    startBtn.classList.remove('opacity-50', 'cursor-not-allowed', 'hidden');
    startBtn.classList.add('hover:opacity-90');

    const finishControls = document.getElementById('finishControls');
    if (finishControls) finishControls.classList.add('hidden');
    const activeControls = document.getElementById('activeControls');
    if (activeControls) activeControls.classList.add('hidden');

    // Boyutları kaydet
    allSizes = sizes || {};

    if (playlist_entries && playlist_entries.length > 0) {
        // ─── Playlist Modu ──────────────────────
        isPlaylistActive = true;
        playlistEntries = playlist_entries;

        document.getElementById('detailsBox').classList.add('hidden');
        document.getElementById('playlistScrollContainer').classList.remove('hidden');
        document.getElementById('playlistTitle').innerText = title;
        document.getElementById('playlistCountSub').innerText = `${playlist_entries.length} Video`;

        // Kapak görseli
        const thumb = document.getElementById('videoThumb');
        if (playlist_entries[0] && playlist_entries[0].thumbnail) {
            thumb.src = playlist_entries[0].thumbnail;
            thumb.classList.remove('max-w-[70%]', 'max-h-[70%]');
            thumb.classList.add('w-full', 'h-full', 'object-cover');
        } else if (playlist_entries[0] && playlist_entries[0].id && currentUrl.includes("youtube")) {
            thumb.src = `https://i.ytimg.com/vi/${playlist_entries[0].id}/hqdefault.jpg`;
            thumb.classList.remove('max-w-[70%]', 'max-h-[70%]');
            thumb.classList.add('w-full', 'h-full', 'object-cover');
        } else if (imgUrl) {
            thumb.src = imgUrl;
            thumb.classList.remove('max-w-[70%]', 'max-h-[70%]');
            thumb.classList.add('w-full', 'h-full', 'object-cover');
        }

        renderPlaylistItems();

    } else {
        // ─── Tekil Video Modu ───────────────────
        isPlaylistActive = false;
        playlistEntries = [];

        document.getElementById('playlistScrollContainer').classList.add('hidden');
        document.getElementById('thumbContainer').classList.remove('hidden');
        document.getElementById('detailsBox').classList.remove('hidden');
        document.getElementById('videoTitle').innerText = title;
        document.getElementById('videoDesc').innerText = "";

        if (imgUrl) {
            const thumb = document.getElementById('videoThumb');
            thumb.src = imgUrl;
            thumb.classList.remove('max-w-[70%]', 'max-h-[70%]');
            thumb.classList.add('w-full', 'h-full', 'object-cover');
        }

        // Seçili çözünürlüğün boyutunu göster
        const badge = document.getElementById('sizeBadge');
        if (allSizes[currentQuality]) {
            badge.innerText = allSizes[currentQuality];
            badge.classList.remove('hidden');
        }
    }

    // Çözünürlük butonlarını güncelle
    if (max_height) {
        updateResolutionButtons(max_height);
    }
}

// ═══════════════════════════════════════════════════════════
//  UI SIFIRLAMA
// ═══════════════════════════════════════════════════════════

function resetUI(force) {
    if (isDownloading && !force) return;

    isDownloading = false;
    isPlaylistActive = false;
    playlistEntries = [];
    allSizes = {};
    enableAllResolutionButtons();

    document.getElementById('playlistScrollContainer').classList.add('hidden');
    document.getElementById('thumbContainer').classList.remove('hidden');
    document.getElementById('detailsBox').classList.remove('hidden');

    document.getElementById('urlInput').value = "";
    document.getElementById('videoTitle').innerText = "Video Bekleniyor...";
    document.getElementById('videoDesc').innerText = "Link yapıştırın, otomatik analiz edilsin.";

    const thumb = document.getElementById('videoThumb');
    thumb.src = LOGO_DATA || "logo.png";
    thumb.classList.add('max-w-[70%]', 'max-h-[70%]');
    thumb.classList.remove('w-full', 'h-full', 'object-cover');

    document.getElementById('sizeBadge').classList.add('hidden');
    document.getElementById('inputLoader').classList.add('hidden');
    document.getElementById('progressBar').style.width = '0%';
    document.getElementById('statusText').innerText = "Sistem Durumu: Çalışıyor";

    const startBtn = document.getElementById('startBtn');
    startBtn.disabled = true;
    startBtn.classList.add('opacity-50', 'cursor-not-allowed');
    startBtn.classList.remove('hover:opacity-90', 'hidden');

    document.getElementById('activeControls').classList.add('hidden');
    const finishControls = document.getElementById('finishControls');
    if (finishControls) finishControls.classList.add('hidden');
    document.getElementById('pauseIcon').innerText = "pause";
    document.getElementById('pauseText').innerText = "DURAKLAT";
    
    // Kesme alanlarını sıfırla
    if (document.getElementById('trimStartInput')) document.getElementById('trimStartInput').value = "";
    if (document.getElementById('trimEndInput')) document.getElementById('trimEndInput').value = "";
    if (document.getElementById('trimInputsContainer')) document.getElementById('trimInputsContainer').classList.add('hidden');
    if (document.getElementById('trimToggleBtn')) document.getElementById('trimToggleBtn').innerText = "+ Kesme Ekle";
}

// ═══════════════════════════════════════════════════════════
//  İNDİRME VE KESME KONTROLLERİ
// ═══════════════════════════════════════════════════════════

function toggleTrimInputs() {
    const container = document.getElementById('trimInputsContainer');
    const btn = document.getElementById('trimToggleBtn');
    if (!container || !btn) return;

    if (container.classList.contains('hidden')) {
        container.classList.remove('hidden');
        btn.innerText = "- Temizle / Kapat";
    } else {
        container.classList.add('hidden');
        document.getElementById('trimStartInput').value = "";
        document.getElementById('trimEndInput').value = "";
        btn.innerText = "+ Kesme Ekle";
    }
}

async function browseFolder() {
    if (window.pywebview && window.pywebview.api) {
        const path = await pywebview.api.browse();
        if (path) {
            document.getElementById('pathDisplay').innerText = path;
        }
    }
}

function startDownload() {
    const url = document.getElementById('urlInput').value;
    const path = document.getElementById('pathDisplay').innerText;
    if (!url) return;

    const startTime = document.getElementById('trimStartInput')?.value?.trim() || "";
    const endTime = document.getElementById('trimEndInput')?.value?.trim() || "";

    isDownloading = true;
    document.getElementById('startBtn').classList.add('hidden');
    document.getElementById('activeControls').classList.remove('hidden');
    document.getElementById('statusText').innerText = "İndirme motoru başlatılıyor...";

    pywebview.api.download(url, currentQuality, path, currentFormat, startTime, endTime);
}

async function togglePause() {
    const isPaused = await pywebview.api.toggle_pause();
    const pauseIcon = document.getElementById('pauseIcon');
    const pauseText = document.getElementById('pauseText');

    if (isPaused) {
        pauseIcon.innerText = "play_arrow";
        pauseText.innerText = "DEVAM ET";
        document.getElementById('statusText').innerText = "Duraklatıldı";
    } else {
        pauseIcon.innerText = "pause";
        pauseText.innerText = "DURAKLAT";
    }
}

function stopDownload() {
    if (window.pywebview && window.pywebview.api) {
        pywebview.api.stop_download();
    }
    document.getElementById('statusText').innerText = "İptal ediliyor...";
    isDownloading = false;
}

// ═══════════════════════════════════════════════════════════
//  İLERLEME & SONUÇ (Python'dan çağrılır)
// ═══════════════════════════════════════════════════════════

function updateProgress(percent, text, plIndex, plTotal) {
    let displayPercent = percent;
    let displayText = text;

    if (plIndex != null && plTotal != null) {
        displayPercent = ((plIndex - 1) * 100 + percent) / plTotal;
        displayText = `(${plIndex}/${plTotal}) ${text}`;
    }

    document.getElementById('progressBar').style.width = displayPercent + '%';
    document.getElementById('statusText').innerText = displayText;
    if (percent === 0) document.getElementById('inputLoader').classList.add('hidden');
}

function finishDownload(success, message) {
    document.getElementById('progressBar').style.width = success ? '100%' : '0%';
    document.getElementById('statusText').innerText = message;
    document.getElementById('inputLoader').classList.add('hidden');

    isDownloading = false;
    
    if (success) {
        // Başarılı ise sıfırlama, bitti butonlarını göster
        document.getElementById('activeControls').classList.add('hidden');
        const finishControls = document.getElementById('finishControls');
        if (finishControls) finishControls.classList.remove('hidden');
    } else {
        // Hata veya iptal durumunda kullanıcı yenileyebilsin veya tekrar deneyebilsin diye arayüzü sıfırlama
        document.getElementById('activeControls').classList.add('hidden');
        const startBtn = document.getElementById('startBtn');
        if (startBtn) {
            startBtn.disabled = false;
            startBtn.classList.remove('opacity-50', 'cursor-not-allowed', 'hidden');
            startBtn.classList.add('hover:opacity-90');
        }
    }
}

function openDownloadFolder() {
    const path = document.getElementById('pathDisplay').innerText;
    if (window.pywebview && window.pywebview.api) {
        pywebview.api.open_download_folder(path);
    }
}

// ═══════════════════════════════════════════════════════════
//  PLAYLİST RENDER
// ═══════════════════════════════════════════════════════════

function updatePlaylistItemSize(index, sizes) {
    if (playlistEntries[index]) {
        playlistEntries[index].sizes = sizes;
        renderPlaylistItems();
    }
}

function renderPlaylistItems() {
    const container = document.getElementById('playlistItems');
    if (!container) return;
    container.innerHTML = "";

    let totalSize = 0;
    let allLoaded = true;

    playlistEntries.forEach((entry, idx) => {
        let sizeStr = "Hesaplanıyor...";
        let sizeVal = 0;

        if (entry.sizes && entry.sizes[currentQuality]) {
            sizeStr = entry.sizes[currentQuality];
            if (sizeStr.includes(" MB")) {
                sizeVal = parseFloat(sizeStr.replace(" MB", ""));
            }
        } else {
            allLoaded = false;
        }
        totalSize += sizeVal;

        const itemDiv = document.createElement('div');
        itemDiv.className = "flex items-center justify-between gap-3 p-2 bg-[#0e0e0e]/50 border border-white/5 rounded-lg text-xs hover:border-[#c0c1ff]/30 transition-all";

        const infoContainer = document.createElement('div');
        infoContainer.className = "flex items-center gap-2 min-w-0 flex-1";

        const indexSpan = document.createElement('span');
        indexSpan.className = "text-primary font-bold w-4 flex-shrink-0 text-right pr-1";
        indexSpan.innerText = `${idx + 1}`;

        const titleSpan = document.createElement('span');
        titleSpan.className = "text-white font-medium truncate";
        titleSpan.innerText = entry.title;

        infoContainer.appendChild(indexSpan);
        infoContainer.appendChild(titleSpan);

        const sizeSpan = document.createElement('span');
        sizeSpan.className = "text-primary font-semibold flex-shrink-0 bg-primary/10 px-1.5 py-0.5 rounded border border-primary/10";
        sizeSpan.innerText = sizeStr;

        itemDiv.appendChild(infoContainer);
        itemDiv.appendChild(sizeSpan);
        container.appendChild(itemDiv);
    });

    const totalText = allLoaded ? `${totalSize.toFixed(1)} MB` : "Hesaplanıyor...";
    document.getElementById('playlistTotalSize').innerText = totalText;
}

// ═══════════════════════════════════════════════════════════
//  ÇÖZÜNÜRLÜK BUTONLARI
// ═══════════════════════════════════════════════════════════

function updateResolutionButtons(maxHeight) {
    const resolutions = [
        { key: '4320', val: 4320 },
        { key: '2160', val: 2160 },
        { key: '1440', val: 1440 },
        { key: '1080', val: 1080 },
        { key: '720',  val: 720 },
        { key: '480',  val: 480 },
        { key: '360',  val: 360 },
    ];
    let highestAvailableKey = '360';
    let isCurrentDisabled = false;

    resolutions.forEach(res => {
        const btn = document.querySelector(`[data-quality="${res.key}"]`);
        if (!btn) return;

        if (res.val > maxHeight) {
            btn.disabled = true;
            btn.classList.add('opacity-30', 'pointer-events-none');
            btn.classList.remove('text-gray-400', 'active');
            if (currentQuality === res.key) isCurrentDisabled = true;
        } else {
            btn.disabled = false;
            btn.classList.remove('opacity-30', 'pointer-events-none');
            const hVal = resolutions.find(r => r.key === highestAvailableKey)?.val || 0;
            if (res.val > hVal) highestAvailableKey = res.key;
        }
    });

    if (isCurrentDisabled) {
        const btn = document.querySelector(`[data-quality="${highestAvailableKey}"]`);
        if (btn) setQuality(highestAvailableKey, btn);
    }
}

function enableAllResolutionButtons() {
    document.querySelectorAll('.res-btn').forEach(btn => {
        btn.disabled = false;
        btn.classList.remove('opacity-30', 'pointer-events-none');
    });
}

// ═══════════════════════════════════════════════════════════
//  RESİM MODALI
// ═══════════════════════════════════════════════════════════

function showFullImage() {
    const thumb = document.getElementById('videoThumb');
    if (!thumb || !thumb.src) return;
    if (thumb.src.endsWith('logo.png') || thumb.src === (LOGO_DATA || '')) return;

    const modal = document.getElementById('imageModal');
    const modalImg = document.getElementById('modalImg');
    modalImg.src = thumb.src;
    modal.classList.remove('hidden');
    modal.offsetHeight;     // Force reflow for transition
    modal.classList.remove('opacity-0');
    modalImg.classList.remove('scale-90');
    modalImg.classList.add('scale-100');
}

function closeFullImage() {
    const modal = document.getElementById('imageModal');
    const modalImg = document.getElementById('modalImg');
    modal.classList.add('opacity-0');
    modalImg.classList.remove('scale-100');
    modalImg.classList.add('scale-90');
    setTimeout(() => modal.classList.add('hidden'), 300);
}

// ═══════════════════════════════════════════════════════════
//  ESKİ API UYUMLULUK (Python eski çağrı yaparsa hata vermesin)
// ═══════════════════════════════════════════════════════════

function updateSizeIfMatch() { /* kullanılmıyor */ }

// ═══════════════════════════════════════════════════════════
//  KLAVYE KISAYOLLARI
// ═══════════════════════════════════════════════════════════

window.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
        const modal = document.getElementById('imageModal');
        if (modal && !modal.classList.contains('hidden')) {
            closeFullImage();
        }
    }
});

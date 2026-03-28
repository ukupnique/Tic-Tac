let currentGameId = null;
let isAiThinking = false; // Флаг чтобы запретить клики пока бот думает

async function createNewGame() {
    hideWinLine(); // Скрываем старую линию
    const response = await fetch('/game', { method: 'POST' });
    const data = await response.json();
    currentGameId = data.game_id;
    updateStatus("Ваш ход (✕)");
    renderBoard(data.board);
}

async function makeMove(row, col) {
    if (!currentGameId || isAiThinking) return;

    // 1. Оптимистичное обновление: рисуем X мгновенно
    const cellId = `cell-${row}-${col}`;
    const clickedCell = document.getElementById(cellId);
    if (clickedCell && !clickedCell.classList.contains('taken')) {
        clickedCell.innerText = '✕';
        clickedCell.classList.add('x', 'taken');
    }

    isAiThinking = true; // Бот начал думать
    updateStatus("Бот анализирует...");

    const response = await fetch(`/game/${currentGameId}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ row, col })
    });
    const data = await response.json();
    
    if (data.error) {
        updateStatus(data.error);
        // Откатываем оптимистичное обновление если ошибка
        createNewGame(); 
        isAiThinking = false;
    } else {
        // Находим, куда сходил бот (где появилась 2)
        const botMove = findBotMove(matrixBefore, data.board);
        
        if (botMove) {
            // Анимация "ИИ думает" над этой клеткой 0.5 сек
            const aiCell = document.getElementById(`cell-${botMove.row}-${botMove.col}`);
            aiCell.classList.add('ai-thinking');
            await sleep(500); // Пауза для красоты
            aiCell.classList.remove('ai-thinking');
        }

        renderBoard(data.board); // Рисуем финальное поле (с 'O')
        isAiThinking = false; // Бот закончил

        if (data.winner !== false) {
            handleGameOver(data.winner);
        } else {
            updateStatus("Ваш ход (✕)");
        }
    }
}

// Хелпер для паузы
const sleep = (ms) => new Promise(r => setTimeout(r, ms));

// Переменная для хранения поля ДО хода бота (нужна для анимации 'ai-thinking')
let matrixBefore = [];

function renderBoard(matrix) {
    matrixBefore = JSON.parse(JSON.stringify(matrix)); // Сохраняем копию
    const boardDiv = document.getElementById('game-board');
    boardDiv.innerHTML = '';
    
    // Создаем элемент линии если его нет
    if (!document.getElementById('win-line')) {
        const line = document.createElement('div');
        line.id = 'win-line';
        line.className = 'winning-line';
        boardDiv.appendChild(line);
    }

    matrix.forEach((row, rIdx) => {
        row.forEach((cell, cIdx) => {
            const cellDiv = document.createElement('div');
            cellDiv.className = 'cell' + (cell !== 0 ? ' taken' : '');
            cellDiv.id = `cell-${rIdx}-${cIdx}`; // ID для анимаций

            if (cell === 1) { cellDiv.innerText = '✕'; cellDiv.classList.add('x'); }
            if (cell === 2) { cellDiv.innerText = '○'; cellDiv.classList.add('o'); }
            cellDiv.onclick = () => { if (cell === 0) makeMove(rIdx, cIdx); };
            boardDiv.appendChild(cellDiv);
        });
    });
}

// Логика завершения игры и рисования линии
function handleGameOver(winner) {
    currentGameId = null; // Сбрасываем ID, чтобы нельзя было ходить после конца
    let msg = "";
    
    // Приводим к числу на случай, если пришла строка
    const winStatus = parseInt(winner); 

    if (winStatus === 1) { 
        msg = "Победа за вами! 🎉"; 
        // Здесь можно активировать красную линию
    } else if (winStatus === 2) { 
        msg = "Бот выиграл! 🤖"; 
        // Здесь можно активировать синюю линию
    } else { 
        msg = "Ничья! 🤝"; 
    }
    
    updateStatus(msg);
}

    // Рисуем линию 

function hideWinLine() {
    const line = document.getElementById('win-line');
    if(line) {
        line.classList.remove('active', 'x-win', 'o-win');
        line.style.cssText = ''; // Сброс координат
    }
}

// Вспомогательная функция для поиска хода бота
function findBotMove(oldMatrix, newMatrix) {
    if (!oldMatrix || oldMatrix.length === 0) return null;
    for (let r = 0; r < 3; r++) {
        for (let c = 0; c < 3; c++) {
            if (oldMatrix[r][c] === 0 && newMatrix[r][c] === 2) {
                return {row: r, col: c};
            }
        }
    }
    return null;
}

function updateStatus(msg) { document.getElementById('status-bar').innerText = msg; }
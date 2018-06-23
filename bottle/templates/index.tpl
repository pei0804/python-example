% rebase('templates/base.tpl')
<div>
    <h3>あなたが捕まえたアワビの特徴は？</h3>
</div>
<form action="/abalone" method="post">
    <fieldest>
    <legend align="left">入力フォーム</legend>
    <div>
        <label for="sex">性別</label>
    </div>
    <div>
        <select id="sex" name="sex">
            <option value="0">メス</option>
            <option value="1">不明</option>
            <option value="2">オス</option>
        </select>
    </div>
    <div>
        <label for="length">殻長</label>
    </div>
    <div>
        <input type="number" id="length" name="length" min="0" required>
    </div>
    <div>
        <label for="diameter">殻幅</label>
    </div>
    <div>
        <input type="number" id="diameter" name="diameter" min="0" required>
    </div>
    <div>
        <label for="weight">重さ</label>
    </div>
    <div>
        <input type="number" id="weight" name="weight" min="0" required>
    </div>
    <div>
        <label for="height">高さ</label>
    </div>
    <div>
        <input type="number" id="height" name="height" min="0" required>
    </div>
    <div class="input-group">
        <input type="submit" value="年齢を当てる">
    </div>
    </fieldest>
</form>

const fs = require('fs');
const path = require('path');
const readline = require('readline/promises');

const DATA_FILE = path.join(__dirname, "data.csv");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

async function getFloat(prompt) {
  while (true) {
    const input = await rl.question(prompt);
    const num = parseFloat(input);
    if (!isNaN(num)) {
      return num;
    }
    console.log("please enter a number");
  }
}

function save(expenses, filename = DATA_FILE) {
  let csvContent = "name,amount\n";
  for (const exp of expenses) {
    csvContent += `${exp.name},${exp.amount}\n`;
  }
  fs.writeFileSync(filename, csvContent);
}

function load(filename = DATA_FILE) {
  const expenses = [];
  try {
    const data = fs.readFileSync(filename, 'utf8');
    const lines = data.trim().split('\n');
    
    for (let i = 1; i < lines.length; i++) {
      const [name, amount] = lines[i].split(',');
      if (name !== undefined && amount !== undefined) {
        expenses.push({ name: name, amount: parseFloat(amount) });
      }
    }
  } catch (error) {
    
    if (error.code === 'ENOENT') {
      
    } else {
      throw error;
    }
  }
  return expenses;
}

(async () => {
  console.log(`
┏┓ ╻ ╻╺┳┓┏━╸┏━╸╺┳╸╻┏┓╻┏━╸   ┏━┓┏━┓┏━┓
┣┻┓┃ ┃ ┃┃┃╺┓┣╸  ┃ ┃┃┗┫┃╺┓   ┣━┫┣━┛┣━┛
┗━┛┗━┛╺┻┛┗━┛┗━╸ ╹ ╹╹ ╹┗━┛   ╹ ╹╹  ╹  
  `);

  const monthly = await getFloat("enter monthly revenue: ");
  let expenses = load();
  let spent = 0;
  
  for (const e of expenses) {
    spent += e.amount;
  }

  while (true) {
    const name = await rl.question("enter name of the expense (done = stop): ");

    if (name === "done") {
      console.log(`you spent ${spent.toFixed(2)} and have ${(monthly - spent).toFixed(2)} left behind`);
      const totals = {};

      for (const e of expenses) {
        const optionName = e.name;
        const amount = e.amount;

        if (optionName in totals) {
          totals[optionName] += amount;
        } else {
          totals[optionName] = amount;
        }
      }

      for (const optionName in totals) {
        console.log(`${optionName}: ${totals[optionName].toFixed(2)}`);
      }

      if ((monthly - spent) >= 0) {
        console.log("you can survive");
      } else {
        console.log("you spent too much");
      }

      save(expenses);
      rl.close();
      break;

    } else {
      const cost = await getFloat("enter cost of expense: ");
      spent = spent + cost;
      expenses.push({ name: name, amount: cost });
    }
  }
})();
# DC Rsync Pipeline

A separate PDF document is provided with **login links and passwords**.

---

## Example 1 – Running a Test Node

1. **Log in** to the test node.  
2. **Open a new shell** and navigate to the GitHub repository folder:
   ```bash
   su teamlary
   cd /home/teamlary/gitHubRepos/iotSystemsGuide/DCNodes/firmware/xu4Mqtt/
   ```

The `DCNodes` folder contains a typical codebase used to operate **Direct-Connect (DC) Nodes** on a single-board computer (SBC).  
At this point, inspect the file [`bme280Reader.py`](https://github.com/mi3nts/iotSystemsGuide/blob/main/DCNodes/firmware/xu4Mqtt/bme280Reader.py), which demonstrates a sample implementation of a **climate sensor** used in our live nodes.

3. **Run the file:**
   ```bash
   python3 bme280Reader.py
   ```

4. **Check where the data is saved.**  
   When adding a new sensor to a unit, use the function `sensorFinisher()` with the corresponding **sensor dictionary**.

The full list of supported sensors and their respective dictionaries can be found here:  
👉 [dcSensorIDs.py](https://github.com/mi3nts/iotSystemsGuide/blob/main/dcSensorIDs.py)

Ensure you:
- Maintain the **same field ordering**  
- Use the **appropriate units**, especially if reusing an existing sensor definition.

---

## Registering DC Nodes on the Rsync Pipeline

The Rsync pipeline uses **SSH key-based authentication** to securely transfer data to our **IMD data server**.  
To register a new DC Node, follow these steps:

---

### 1. Generate an SSH Key on the Node
```bash
ssh-keygen
```

---

### 2. Copy the SSH Public Key

---

### 3. Add the Key to the IMD Server
Log in to the IMD data server:
```bash
ssh mints@mintsdata.utdallas.edu -p 2222
```

Once logged in:
```bash
cd ~/.ssh
vim authorized_keys
```
Paste the node’s SSH public key into the `authorized_keys` file.

> ⚠️ **Note:** You must already have access to the IMD server before performing this step.

---

### 4. Verify SSH Access from the Node
Return to the node and confirm that it can access the IMD server:
```bash
ssh mints@mintsdata.utdallas.edu -p 2222
```

---

### 5. Sync Data to IMD
Manually run Rsync to verify connectivity and data transfer:
```bash
rsync -avzrtu -e "ssh -p 2222" /home/teamlary/mintsData/raw/ mints@mintsdata.utdallas.edu:raw
```

After running Rsync, check the IMD server to confirm that the data has been successfully transferred.

---

### 6. Automate Rsync with Cron
To automatically sync data every minute, add the following line to the node’s **crontab**:
```bash
* * * * * rsync -avzrtu -e "ssh -p 2222" /home/teamlary/mintsData/raw/ mints@mintsdata.utdallas.edu:raw
```

This ensures that your node’s data is continuously mirrored to the IMD server in near real time.

---

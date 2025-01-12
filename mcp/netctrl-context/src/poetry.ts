import { exec } from "child_process";
import { promisify } from "util";
import path from "path";
import fs from "fs/promises";
import yaml from "yaml";

const execAsync = promisify(exec);

export class PoetryManager {
  private projectRoot: string;

  constructor(projectRoot: string) {
    this.projectRoot = projectRoot;
  }

  async getVirtualEnvPath(): Promise<string | null> {
    try {
      const { stdout } = await execAsync("poetry env info --path", {
        cwd: this.projectRoot
      });
      return stdout.trim();
    } catch {
      return null;
    }
  }

  async getDependencies(): Promise<{
    dependencies: Record<string, string>;
    devDependencies: Record<string, string>;
  }> {
    try {
      const pyprojectPath = path.join(this.projectRoot, "pyproject.toml");
      const content = await fs.readFile(pyprojectPath, "utf-8");
      
      // Parse TOML content
      const lines = content.split("\n");
      const dependencies: Record<string, string> = {};
      const devDependencies: Record<string, string> = {};
      
      let inDependencies = false;
      let inDevDependencies = false;
      
      for (const line of lines) {
        if (line.trim() === "[tool.poetry.dependencies]") {
          inDependencies = true;
          inDevDependencies = false;
          continue;
        }
        if (line.trim() === "[tool.poetry.group.dev.dependencies]") {
          inDependencies = false;
          inDevDependencies = true;
          continue;
        }
        if (line.trim().startsWith("[")) {
          inDependencies = false;
          inDevDependencies = false;
          continue;
        }
        
        if (inDependencies || inDevDependencies) {
          const match = line.match(/^([^=]+)\s*=\s*"([^"]+)"/);
          if (match) {
            const [, name, version] = match;
            if (inDependencies) {
              dependencies[name.trim()] = version.trim();
            } else {
              devDependencies[name.trim()] = version.trim();
            }
          }
        }
      }

      return { dependencies, devDependencies };
    } catch (error) {
      console.error("Error parsing pyproject.toml:", error);
      return {
        dependencies: {},
        devDependencies: {}
      };
    }
  }

  async getProjectInfo(): Promise<{
    name: string;
    version: string;
    description?: string;
  } | null> {
    try {
      const pyprojectPath = path.join(this.projectRoot, "pyproject.toml");
      const content = await fs.readFile(pyprojectPath, "utf-8");
      
      const lines = content.split("\n");
      let inToolPoetry = false;
      const info: Record<string, string> = {};
      
      for (const line of lines) {
        if (line.trim() === "[tool.poetry]") {
          inToolPoetry = true;
          continue;
        }
        if (line.trim().startsWith("[") && line.trim() !== "[tool.poetry]") {
          inToolPoetry = false;
          continue;
        }
        
        if (inToolPoetry) {
          const match = line.match(/^([^=]+)\s*=\s*"([^"]+)"/);
          if (match) {
            const [, key, value] = match;
            info[key.trim()] = value.trim();
          }
        }
      }
      
      if (!info.name || !info.version) {
        return null;
      }
      
      return {
        name: info.name,
        version: info.version,
        description: info.description
      };
    } catch {
      return null;
    }
  }
}

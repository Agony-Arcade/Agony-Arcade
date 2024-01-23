# Repository Guidelines

Our repository follows a set of guidelines to ensure a standardized and organized development process. Adhering to these norms contributes to a cohesive and efficient collaborative environment.

## Branching Conventions:

### Branch Naming:

- **Feature Branches:** Use the format `BRx-feature-BRANCH NAME` for branches dedicated to implementing new features.
- **Fix Branches:** Utilize the format `BRx-fix-BRANCH NAME` for branches intended for bug fixes.

## Pull Request (PR):

### Naming Convention:

When creating a pull request, provide a clear and concise name that summarizes the changes introduced in the branch.

### Commit Message Convention:

#### Structure:

For commits within branches, follow the convention:
- **Feature:** `feature(): commit msg`
- **Fix:** `fix(): commit msg`
Prefix each commit with either `feature()` or `fix()` to indicate the nature of the changes.

#### Example:

BR1-feature-user-authentication
├── feature(): Add user authentication functionality
├── feature(): Implement login and registration
├── fix(): Resolve authentication bug in user registration
├── feature(): Enhance password reset mechanism
└── fix(): Fix session timeout issue

